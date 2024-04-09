import bpy
from bpy.types import PropertyGroup
from bpy.props import StringProperty
from bpy.props import PointerProperty
from bpy.props import BoolProperty
from bpy.props import EnumProperty

from collections import OrderedDict

from . import preset_handler
from .utils import make_annotations


class RetargetBase():
    def has_settings(self):
        for k in self.keys():
            if k == 'name':
                continue
            v = getattr(self, k, None)
            if v:
                if hasattr(v, "has_settings"):
                    if not v.has_settings():
                        continue
                return True
        return False

    def _as_dict(self, base=''):
        "returns all props with dot-delimited keys"
        _res = OrderedDict()
        if hasattr(self, "_order"):
            _items = self._order
        else:
            _items = self.rna_type.properties.keys()
        for _attr in _items:
            if _attr in ("rna_type", "name") or not hasattr(self, _attr):
                continue
            _prop = getattr(self, _attr)
            _subattrs = getattr(_prop, '_as_dict', None)
            if _prop and _subattrs:
                _res.update(_prop._as_dict(base=(base + "." if base else "") + _attr))
            else:
                _res[(base + "." if base else "") + _attr] = _prop
        return _res

    def _set_from_dict(self, d, base=''):
        "sets props given in the dict with dot-delimited keys"
        _attrs = []
        _baselen = len(base) + 1
        for k, v in d.items():
            if base and k.startswith(base):
                k = k[_baselen:]
            _attrs.clear()
            _attrs.extend(k.split("."))
            if _attrs[-1] == "name":
                continue
            _prop = self
            for _attr in _attrs[:-1]:
                if not hasattr(_prop, _attr):
                    continue
                _prop = getattr(_prop, _attr)
            if not hasattr(_prop, _attrs[-1]):
                continue
            _t = type(getattr(_prop, _attrs[-1]))
            if _t is bool:
                v = v.lower() in ("true", "1", "y", "yes")
            elif _t is not str:
                v = _t(v)
            setattr(_prop, _attrs[-1], v)


@make_annotations
class RetargetSpine(RetargetBase, PropertyGroup):
    _order = ("head", "neck", "spine2", "spine1", "spine", "hips")

    head = StringProperty(name="head")
    neck = StringProperty(name="neck")
    spine2 = StringProperty(name="spine2")
    spine1 = StringProperty(name="spine1")
    spine = StringProperty(name="spine")
    hips = StringProperty(name="hips")


@make_annotations
class RetargetArm(RetargetBase, PropertyGroup):
    _order = ("shoulder", "arm", "arm_twist", "arm_twist_02", "forearm", "forearm_twist",
              "forearm_twist_02", "hand")

    shoulder = StringProperty(name="shoulder")
    arm = StringProperty(name="arm")
    arm_twist = StringProperty(name="arm_twist")
    arm_twist_02 = StringProperty(name="arm_twist_02")
    forearm = StringProperty(name="forearm")
    forearm_twist = StringProperty(name="forearm_twist")
    forearm_twist_02 = StringProperty(name="forearm_twist_02")
    hand = StringProperty(name="hand")

    name = StringProperty(default='arm')


@make_annotations
class RetargetLeg(RetargetBase, PropertyGroup):
    _order = ("upleg", "upleg_twist", "upleg_twist_02", "leg", "leg_twist", "leg_twist_02",
              "foot", "toe")

    upleg = StringProperty(name="upleg")
    upleg_twist = StringProperty(name="upleg_twist")
    upleg_twist_02 = StringProperty(name="upleg_twist_02")
    leg = StringProperty(name="leg")
    leg_twist = StringProperty(name="leg_twist")
    leg_twist_02 = StringProperty(name="leg_twist_02")
    foot = StringProperty(name="foot")
    toe = StringProperty(name="toe")

    name = StringProperty(default='leg')


@make_annotations
class RetargetFinger(RetargetBase, PropertyGroup):
    _order = ("meta", "a", "b", "c")

    meta = StringProperty(name="meta")
    a = StringProperty(name="A")
    b = StringProperty(name="B")
    c = StringProperty(name="C")


@make_annotations
class RetargetFingers(RetargetBase, PropertyGroup):
    _order = ("thumb", "index", "middle", "ring", "pinky")

    thumb = PointerProperty(type=RetargetFinger)
    index = PointerProperty(type=RetargetFinger)
    middle = PointerProperty(type=RetargetFinger)
    ring = PointerProperty(type=RetargetFinger)
    pinky = PointerProperty(type=RetargetFinger)

    name = StringProperty(default='fingers')


@make_annotations
class RetargetFaceSimple(RetargetBase, PropertyGroup):
    _order = ("jaw", "right_eye", "left_eye", "right_upLid", "left_upLid", "super_copy")

    jaw = StringProperty(name="jaw")
    left_eye = StringProperty(name="left_eye")
    right_eye = StringProperty(name="right_eye")

    left_upLid = StringProperty(name="left_upLid")
    right_upLid = StringProperty(name="right_upLid")

    super_copy = BoolProperty(default=True)


@make_annotations
class RetargetSettings(RetargetBase, PropertyGroup):
    _order = ("face", "spine",
              "right_arm", "left_arm",
              "right_leg", "left_leg",
              "right_fingers", "left_fingers",
              "right_arm_ik", "left_arm_ik",
              "right_leg_ik", "left_leg_ik",
              "root", "deform_preset")

    face = PointerProperty(type=RetargetFaceSimple)
    spine = PointerProperty(type=RetargetSpine)

    left_arm = PointerProperty(type=RetargetArm)
    left_arm_ik = PointerProperty(type=RetargetArm)
    left_fingers = PointerProperty(type=RetargetFingers)

    right_arm = PointerProperty(type=RetargetArm)
    right_arm_ik = PointerProperty(type=RetargetArm)
    right_fingers = PointerProperty(type=RetargetFingers)

    left_leg = PointerProperty(type=RetargetLeg)
    left_leg_ik = PointerProperty(type=RetargetLeg)
    right_leg = PointerProperty(type=RetargetLeg)
    right_leg_ik = PointerProperty(type=RetargetLeg)

    root = StringProperty(name="root")

    deform_preset = EnumProperty(items=preset_handler.iterate_presets, name="Deformation Bones")

    last_used_preset = StringProperty(
        name="Last used preset", default="", description="Preset from which the settings were loaded from (or saved to).",
        options={'SKIP_SAVE','HIDDEN'}) # base name, not a full path

    def has_settings(self):
        for setting in (self.spine, self.left_arm, self.left_arm_ik, self.left_fingers,
                        self.right_arm, self.right_arm_ik, self.right_fingers,
                        self.left_leg, self.left_leg_ik, self.right_leg, self.right_leg_ik):
            if setting.has_settings():
                return True

        return False


def register_classes():
    bpy.utils.register_class(RetargetSpine)
    bpy.utils.register_class(RetargetArm)
    bpy.utils.register_class(RetargetLeg)
    bpy.utils.register_class(RetargetFinger)
    bpy.utils.register_class(RetargetFingers)
    bpy.utils.register_class(RetargetFaceSimple)

    bpy.utils.register_class(RetargetSettings)
    bpy.types.Armature.expykit_retarget = PointerProperty(type=RetargetSettings)
    bpy.types.Armature.expykit_twist_on = BoolProperty(default=False)


def unregister_classes():
    del bpy.types.Armature.expykit_retarget
    del bpy.types.Armature.expykit_twist_on

    bpy.utils.unregister_class(RetargetSettings)

    bpy.utils.unregister_class(RetargetFaceSimple)
    bpy.utils.unregister_class(RetargetFingers)
    bpy.utils.unregister_class(RetargetFinger)
    bpy.utils.unregister_class(RetargetSpine)

    bpy.utils.unregister_class(RetargetArm)
    bpy.utils.unregister_class(RetargetLeg)
