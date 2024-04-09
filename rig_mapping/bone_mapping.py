

rigify_face_bones = (
    'face', 'nose', 'nose.001', 'nose.002', 'nose.003', 'nose.004',
    'lip.T.L', 'lip.T.L.001', 'lip.B.L', 'lip.B.L.001',
    'jaw', 'chin', 'chin.001',
    'ear.L', 'ear.L.001', 'ear.L.002', 'ear.L.003', 'ear.L.004', 'ear.R', 'ear.R.001', 'ear.R.002', 'ear.R.003', 'ear.R.004',
    'lip.T.R', 'lip.T.R.001', 'lip.B.R', 'lip.B.R.001',
    'brow.B.L', 'brow.B.L.001', 'brow.B.L.002', 'brow.B.L.003',
    'lid.T.L', 'lid.T.L.001', 'lid.T.L.002', 'lid.T.L.003', 'lid.B.L', 'lid.B.L.001', 'lid.B.L.002', 'lid.B.L.003',
    'brow.B.R', 'brow.B.R.001', 'brow.B.R.002', 'brow.B.R.003',
    'lid.T.R', 'lid.T.R.001', 'lid.T.R.002', 'lid.T.R.003',
    'lid.B.R', 'lid.B.R.001', 'lid.B.R.002', 'lid.B.R.003',
    'forehead.L', 'forehead.L.001', 'forehead.L.002',  'temple.L',
    'jaw.L', 'jaw.L.001', 'chin.L', 'cheek.B.L', 'cheek.B.L.001',
    'brow.T.L', 'brow.T.L.001', 'brow.T.L.002', 'brow.T.L.003',
    'forehead.R', 'forehead.R.001', 'forehead.R.002', 'temple.R',
    'jaw.R', 'jaw.R.001', 'chin.R', 'cheek.B.R', 'cheek.B.R.001',
    'brow.T.R', 'brow.T.R.001', 'brow.T.R.002', 'brow.T.R.003',
    'eye.L', 'eye.R',
    'cheek.T.L', 'cheek.T.L.001', 'cheek.T.R', 'cheek.T.R.001',
    'nose.L', 'nose.L.001', 'nose.R', 'nose.R.001',
    'teeth.T', 'teeth.B', 'tongue', 'tongue.001', 'tongue.002',
)

rigify_version = None

class HumanLimb:
    def __str__(self):
        return self.__class__.__name__ + ' ' + ', '.join(["{0}: {1}".format(k, v) for k, v in self.__dict__.items()])

    def __getitem__(self, item):
        return getattr(self, item, None)

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def has_settings(self):
        return bool(self)


class SimpleFace(HumanLimb):
    def __init__(self, jaw='', left_eye='', right_eye=''):
        self.jaw = jaw
        self.left_eye = left_eye
        self.right_eye = right_eye

        self.super_copy = True


class HumanSpine(HumanLimb):
    def __init__(self, head='', neck='', spine2='', spine1='', spine='', hips=''):
        self.head = head
        self.neck = neck
        self.spine2 = spine2
        self.spine1 = spine1
        self.spine = spine
        self.hips = hips


class HumanArm(HumanLimb):
    def __init__(self, shoulder='', arm='', forearm='', hand=''):
        self.shoulder = shoulder
        self.arm = arm
        self.arm_twist = None
        self.arm_twist_02 = None
        self.forearm = forearm
        self.forearm_twist = None
        self.forearm_twist_02 = None
        self.hand = hand


class HumanLeg(HumanLimb):
    def __init__(self, upleg='', leg='', foot='', toe=''):
        self.upleg = upleg
        self.upleg_twist = None
        self.upleg_twist_02 = None
        self.leg = leg
        self.leg_twist = None
        self.leg_twist_02 = None
        self.foot = foot
        self.toe = toe


class HumanFingers(HumanLimb):
    def __init__(self, thumb=[''] * 4, index=[''] * 4, middle=[''] * 4, ring=[''] * 4, pinky=[''] * 4, preset=None):
        if preset:
            self.thumb = [preset.thumb.a, preset.thumb.b, preset.thumb.c, preset.thumb.meta]
            self.index = [preset.index.a, preset.index.b, preset.index.c, preset.index.meta]
            self.middle = [preset.middle.a, preset.middle.b, preset.middle.c, preset.middle.meta]
            self.ring = [preset.ring.a, preset.ring.b, preset.ring.c, preset.ring.meta]
            self.pinky = [preset.pinky.a, preset.pinky.b, preset.pinky.c, preset.pinky.meta]
        else:
            self.thumb = thumb
            self.index = index
            self.middle = middle
            self.ring = ring
            self.pinky = pinky


class HumanSkeleton:
    face = None
    root = None
    spine = None

    left_arm = None
    right_arm = None
    left_leg = None
    right_leg = None

    _left_arm_ik = None
    _right_arm_ik = None
    _left_leg_ik = None
    _right_leg_ik = None
    _fk_as_ik = True

    left_fingers = None
    right_fingers = None

    def __init__(self, preset=None):
        if preset:
            self.face = preset.face
            self.spine = preset.spine
            self.left_arm = preset.left_arm
            self._left_arm_ik = preset.left_arm_ik
            self.left_leg = preset.left_leg
            self._left_leg_ik = preset.left_leg_ik

            self.right_arm = preset.right_arm
            self._right_arm_ik = preset.right_arm_ik
            self.right_leg = preset.right_leg
            self._right_leg_ik = preset.right_leg_ik

            self.left_fingers = HumanFingers(preset=preset.left_fingers)
            self.right_fingers = HumanFingers(preset=preset.right_fingers)

            self.root = preset.root

    @property
    def deformation_bone_map(self):
        """Property for control skeletons"""
        return None

    @property
    def left_arm_ik(self):
        if self._left_arm_ik and self._left_arm_ik.has_settings():
            return self._left_arm_ik

        if self._fk_as_ik:
            return self.left_arm

        return None

    @property
    def right_arm_ik(self):
        if self._right_arm_ik and self._right_arm_ik.has_settings():
            return self._right_arm_ik

        if self._fk_as_ik:
            return self.right_arm

        return None

    @property
    def left_leg_ik(self):
        if self._left_leg_ik and self._left_leg_ik.has_settings():
            return self._left_leg_ik

        if self._fk_as_ik:
            return self.left_leg

        return None

    @property
    def right_leg_ik(self):
        if self._right_leg_ik and self._right_leg_ik.has_settings():
            return self._right_leg_ik

        if self._fk_as_ik:
            return self.right_leg

        return None

    @left_arm_ik.setter
    def left_arm_ik(self, value):
        self._left_arm_ik = value

    @right_arm_ik.setter
    def right_arm_ik(self, value):
        self._right_arm_ik = value

    @left_leg_ik.setter
    def left_leg_ik(self, value):
        self._left_leg_ik = value

    @right_leg_ik.setter
    def right_leg_ik(self, value):
        self._right_leg_ik = value

    def bone_names(self):
        if self.root:
            yield self.root

        for limb_name, bone_name in self.spine.items():
            yield bone_name

        for limb_name, bone_name in self.left_arm.items():
            yield bone_name

        for limb_name, bone_name in self.right_arm.items():
            yield bone_name

        for limb_name, bone_name in self.left_leg.items():
            yield bone_name

        for limb_name, bone_name in self.right_leg.items():
            yield bone_name

        if self.left_arm_ik:
            for limb_name, bone_name in self.left_arm_ik.items():
                yield bone_name

        if self.right_arm_ik:
            for limb_name, bone_name in self.right_arm_ik.items():
                yield bone_name

        if self.left_leg_ik:
            for limb_name, bone_name in self.left_leg_ik.items():
                yield bone_name

        if self.right_leg_ik:
            for limb_name, bone_name in self.right_leg_ik.items():
                yield bone_name

        for limb_name, bone_names in self.left_fingers.items():
            for bone_name in bone_names:
                yield bone_name

        for limb_name, bone_names in self.right_fingers.items():
            for bone_name in bone_names:
                yield bone_name

    def conversion_map(self, target_skeleton, skip_ik=False):
        """Return a dictionary that maps skeleton bone names to target bone names
        >>> rigify = RigifySkeleton()
        >>> rigify.conversion_map(MixamoSkeleton())
        {'DEF-spine.006': 'Head', 'DEF-spine.004': 'Neck', 'DEF-spine.003'...
        """
        bone_map = dict()

        def bone_mapping(attr, limb, bone_name):
            if not bone_name:
                return

            target_limbs = getattr(target_skeleton, attr, None)
            if not target_limbs:
                return

            trg_name = getattr(target_limbs, limb, None)

            if trg_name:
                bone_map[bone_name] = trg_name

        if self.root:
            bone_map[self.root] = target_skeleton.root

        face_map = self.face
        if face_map:
            for limb_name, bone_name in face_map.items():
                if limb_name == "super_copy":
                    continue
                bone_mapping('face', limb_name, bone_name)

        for limb_name, bone_name in self.spine.items():
            bone_mapping('spine', limb_name, bone_name)

        if not skip_ik:
            if self.left_arm_ik:
                for limb_name, bone_name in self.left_arm_ik.items():
                    if bone_name == self.left_arm[limb_name]:
                        continue
                    bone_mapping('left_arm_ik', limb_name, bone_name)

            if self.right_arm_ik:
                for limb_name, bone_name in self.right_arm_ik.items():
                    if bone_name == self.right_arm[limb_name]:
                        continue
                    bone_mapping('right_arm_ik', limb_name, bone_name)

            if self.left_leg_ik:
                for limb_name, bone_name in self.left_leg_ik.items():
                    if bone_name == self.left_leg[limb_name]:
                        continue
                    bone_mapping('left_leg_ik', limb_name, bone_name)

            if self.right_leg_ik:
                for limb_name, bone_name in self.right_leg_ik.items():
                    if bone_name == self.right_leg[limb_name]:
                        continue
                    bone_mapping('right_leg_ik', limb_name, bone_name)

        for limb_name, bone_name in self.left_arm.items():
            bone_mapping('left_arm', limb_name, bone_name)

        for limb_name, bone_name in self.right_arm.items():
            bone_mapping('right_arm', limb_name, bone_name)

        for limb_name, bone_name in self.left_leg.items():
            bone_mapping('left_leg', limb_name, bone_name)

        for limb_name, bone_name in self.right_leg.items():
            bone_mapping('right_leg', limb_name, bone_name)

        def fingers_mapping(src_fingers, trg_fingers):
            for finger, bone_names in src_fingers.items():
                trg_bone_names = trg_fingers[finger]

                for bone, trg_bone in zip(bone_names, trg_bone_names):
                    if bone and trg_bone:
                        bone_map[bone] = trg_bone

        trg_fingers = target_skeleton.left_fingers
        fingers_mapping(self.left_fingers, trg_fingers)

        trg_fingers = target_skeleton.right_fingers
        fingers_mapping(self.right_fingers, trg_fingers)

        return bone_map

    def _as_dict(self, base=""):

        def limb_as_dict(limb, base):
            _d = {}
            if getattr(limb, "__dict__", None):
                for k, v in limb.__dict__.items():
                    if k == "name":
                        continue
                    if getattr(v, "__dict__", None):
                        _d.update(limb_as_dict(v, k if not base else base+"."+k))
                    elif isinstance(v, list):
                        _d.update({(k if not base else base+"."+k)+"."+kk : v for kk,v in zip(("a", "b", "c", "meta"), v)})
                    else:
                        _d[k if not base else base+"."+k] = v
                return _d
            else:
                return {base : limb}

        return limb_as_dict(self, base)


class MixamoSkeleton(HumanSkeleton):
    def __init__(self):
        self.spine = HumanSpine(
            head='Head',
            neck='Neck',
            spine2='Spine2',
            spine1='Spine1',
            spine='Spine',
            hips='Hips'
        )

        side = 'Left'
        self.left_arm = HumanArm(shoulder=side + "Shoulder",
                                 arm=side + "Arm",
                                 forearm=side + "ForeArm",
                                 hand=side + "Hand")

        self.left_fingers = HumanFingers(
                    thumb=["{0}HandThumb{1}".format(side, i) for i in range(1, 4)],
                    index=["{0}HandIndex{1}".format(side, i) for i in range(1, 4)],
                    middle=["{0}HandMiddle{1}".format(side, i) for i in range(1, 4)],
                    ring=["{0}HandRing{1}".format(side, i) for i in range(1, 4)],
                    pinky=["{0}HandPinky{1}".format(side, i) for i in range(1, 4)],
                )

        self.left_leg = HumanLeg(upleg="{0}UpLeg".format(side),
                                  leg="{0}Leg".format(side),
                                  foot="{0}Foot".format(side),
                                  toe="{0}ToeBase".format(side))

        side = 'Right'
        self.right_arm = HumanArm(shoulder=side + "Shoulder",
                                 arm=side + "Arm",
                                 forearm=side + "ForeArm",
                                 hand=side + "Hand")

        self.right_fingers = HumanFingers(
            thumb=["{0}HandThumb{1}".format(side, i) for i in range(1, 4)],
            index=["{0}HandIndex{1}".format(side, i) for i in range(1, 4)],
            middle=["{0}HandMiddle{1}".format(side, i) for i in range(1, 4)],
            ring=["{0}HandRing{1}".format(side, i) for i in range(1, 4)],
            pinky=["{0}HandPinky{1}".format(side, i) for i in range(1, 4)],
        )

        self.right_leg = HumanLeg(upleg="{0}UpLeg".format(side),
                                  leg="{0}Leg".format(side),
                                  foot="{0}Foot".format(side),
                                  toe="{0}ToeBase".format(side))


class DazGenesis8(HumanSkeleton):
    def __init__(self):
        self.spine = HumanSpine(
            head='head',
            neck='neckLower',
            spine2='chestLower',
            spine1='abdomenUpper',
            spine='abdomenLower',
            hips='hip'
        )
        self.root = 'root'

        for side, side_letter in zip(('left', 'right'), ('l', 'r')):
            arm = HumanArm(shoulder="{0}Collar".format(side_letter),
                           arm="{0}ShldrBend".format(side_letter),
                           forearm="{0}ForearmBend".format(side_letter),
                           hand="{0}Hand".format(side_letter))

            arm.arm_twist = arm.arm.replace("Bend", "Twist")
            arm.forearm_twist = arm.forearm.replace("Bend", "Twist")
            setattr(self, "{}_arm".format(side), arm)

            fingers = HumanFingers(
                thumb=["{0}Thumb{1}".format(side_letter, i) for i in range(1, 4)],
                index=["{0}Index{1}".format(side_letter, i) for i in range(1, 4)],
                middle=["{0}Mid{1}".format(side_letter, i) for i in range(1, 4)],
                ring=["{0}Ring{1}".format(side_letter, i) for i in range(1, 4)],
                pinky=["{0}Pinky{1}".format(side_letter, i) for i in range(1, 4)],
            )
            setattr(self, side + "_fingers", fingers)

            leg = HumanLeg(upleg="{0}ThighBend".format(side_letter),
                           leg="{0}Shin".format(side_letter),
                           foot="{0}Foot".format(side_letter),
                           toe="{0}Toe".format(side_letter))

            leg.upleg_twist = leg.upleg.replace("Bend", "Twist")
            leg.leg_twist = leg.leg.replace("Bend", "Twist")
            setattr(self, side + "_leg", leg)


class RigifySkeleton(HumanSkeleton):
    def __init__(self):
        if rigify_version >= (0, 5):
            self.face = SimpleFace(
                jaw='DEF-jaw',
                left_eye='DEF-eye.L',
                right_eye='DEF-eye.R'
            )

            self.spine = HumanSpine(
                head='DEF-spine.006',
                neck='DEF-spine.004',
                spine2='DEF-spine.003',
                spine1='DEF-spine.002',
                spine='DEF-spine.001',
                hips='DEF-spine'
            )
        else:
            self.face = SimpleFace()

            self.spine = HumanSpine(
                head='DEF-head',
                neck='DEF-neck',
                spine2='DEF-chest',
                spine1='',
                spine='DEF-spine',
                hips='DEF-hips'
            )


        self.root = 'root'

        for side, side_letter in zip(('left', 'right'), ('L', 'R')):
            if rigify_version >= (0, 5):
                arm = HumanArm(shoulder="DEF-shoulder.{0}".format(side_letter),
                               arm="DEF-upper_arm.{0}".format(side_letter),
                               forearm="DEF-forearm.{0}".format(side_letter),
                               hand="DEF-hand.{0}".format(side_letter))

                arm.arm_twist = arm.arm + ".001"
                arm.forearm_twist = arm.forearm + ".001"
            else:
                arm = HumanArm(shoulder="DEF-shoulder.{0}".format(side_letter),
                               arm="DEF-upper_arm.01.{0}".format(side_letter),
                               forearm="DEF-forearm.01.{0}".format(side_letter),
                               hand="DEF-hand.{0}".format(side_letter))

                arm.arm_twist = arm.arm.replace("01", "02")
                arm.forearm_twist = arm.forearm.replace("01", "02")

            setattr(self, side + "_arm", arm)

            if rigify_version >= (0, 5):
                fingers = HumanFingers(
                    thumb=["DEF-thumb.{1:02d}.{0}".format(side_letter, i) for i in range(1, 4)],
                    index=["DEF-f_index.{1:02d}.{0}".format(side_letter, i) for i in range(1, 4)] + ["DEF-palm.01.{}".format(side_letter)],
                    middle=["DEF-f_middle.{1:02d}.{0}".format(side_letter, i) for i in range(1, 4)] + ["DEF-palm.02.{}".format(side_letter)],
                    ring=["DEF-f_ring.{1:02d}.{0}".format(side_letter, i) for i in range(1, 4)] + ["DEF-palm.03.{}".format(side_letter)],
                    pinky=["DEF-f_pinky.{1:02d}.{0}".format(side_letter, i) for i in range(1, 4)] + ["DEF-palm.04.{}".format(side_letter)],
                )
            else:
                fingers = HumanFingers(
                    thumb=["DEF-thumb.01.{0}.01".format(side_letter)] + ["DEF-thumb.{1:02d}.{0}".format(side_letter, i) for i in range(2, 4)],
                    index=["DEF-f_index.01.{0}.01".format(side_letter)] + ["DEF-f_index.{1:02d}.{0}".format(side_letter, i) for i in range(2, 4)] + ["DEF-palm.01.{}".format(side_letter)],
                    middle=["DEF-f_middle.01.{0}.01".format(side_letter)] + ["DEF-f_middle.{1:02d}.{0}".format(side_letter, i) for i in range(2, 4)] + ["DEF-palm.02.{}".format(side_letter)],
                    ring=["DEF-f_ring.01.{0}.01".format(side_letter)] + ["DEF-f_ring.{1:02d}.{0}".format(side_letter, i) for i in range(2, 4)] + ["DEF-palm.03.{}".format(side_letter)],
                    pinky=["DEF-f_pinky.01.{0}.01".format(side_letter)] + ["DEF-f_pinky.{1:02d}.{0}".format(side_letter, i) for i in range(2, 4)] + ["DEF-palm.04.{}".format(side_letter)],
                )
            setattr(self, side + "_fingers", fingers)

            if rigify_version >= (0, 5):
                leg = HumanLeg(upleg="DEF-thigh.{0}".format(side_letter),
                               leg="DEF-shin.{0}".format(side_letter),
                               foot="DEF-foot.{0}".format(side_letter),
                               toe="DEF-toe.{0}".format(side_letter))

                leg.upleg_twist = leg.upleg + ".001"
                leg.leg_twist = leg.leg + ".001"
            else:
                leg = HumanLeg(upleg="DEF-thigh.01.{0}".format(side_letter),
                               leg="DEF-shin.01.{0}".format(side_letter),
                               foot="DEF-foot.{0}".format(side_letter),
                               toe="DEF-toe.{0}".format(side_letter))

                leg.upleg_twist = leg.upleg.replace("01","02")
                leg.leg_twist = leg.leg.replace("01","02")

            setattr(self, side + "_leg", leg)


class RigifyMeta(HumanSkeleton):
    def __init__(self):
        if rigify_version >= (0, 5):
            self.face = SimpleFace(
                jaw='jaw',
                left_eye='eye.L',
                right_eye='eye.R'
            )

            self.spine = HumanSpine(
                head='spine.006',
                neck='spine.004',
                spine2='spine.003',
                spine1='spine.002',
                spine='spine.001',
                hips='spine'
            )
        else:
            self.face = SimpleFace()

            self.spine = HumanSpine(
                head='head',
                neck='neck',
                spine2='chest',
                spine1='',
                spine='spine',
                hips='hips'
            )

        side = 'L'
        self.left_arm = HumanArm(shoulder="shoulder.{0}".format(side),
                                 arm="upper_arm.{0}".format(side),
                                 forearm="forearm.{0}".format(side),
                                 hand="hand.{0}".format(side))

        self.left_fingers = HumanFingers(
            thumb=["thumb.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            index=["f_index.{1:02d}.{0}".format(side, i) for i in range(1, 4)] + ["palm.01.{}".format(side)],
            middle=["f_middle.{1:02d}.{0}".format(side, i) for i in range(1, 4)] + ["palm.02.{}".format(side)],
            ring=["f_ring.{1:02d}.{0}".format(side, i) for i in range(1, 4)] + ["palm.03.{}".format(side)],
            pinky=["f_pinky.{1:02d}.{0}".format(side, i) for i in range(1, 4)] + ["palm.04.{}".format(side)],
        )

        self.left_leg = HumanLeg(upleg="thigh.{0}".format(side),
                                 leg="shin.{0}".format(side),
                                 foot="foot.{0}".format(side),
                                 toe="toe.{0}".format(side))

        side = 'R'
        self.right_arm = HumanArm(shoulder="shoulder.{0}".format(side),
                                  arm="upper_arm.{0}".format(side),
                                  forearm="forearm.{0}".format(side),
                                  hand="hand.{0}".format(side))

        self.right_fingers = HumanFingers(
            thumb=["thumb.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            index=["f_index.{1:02d}.{0}".format(side, i) for i in range(1, 4)] + ["palm.01.{}".format(side)],
            middle=["f_middle.{1:02d}.{0}".format(side, i) for i in range(1, 4)] + ["palm.02.{}".format(side)],
            ring=["f_ring.{1:02d}.{0}".format(side, i) for i in range(1, 4)] + ["palm.03.{}".format(side)],
            pinky=["f_pinky.{1:02d}.{0}".format(side, i) for i in range(1, 4)] + ["palm.04.{}".format(side)],
        )

        self.right_leg = HumanLeg(upleg="thigh.{0}".format(side),
                                  leg="shin.{0}".format(side),
                                  foot="foot.{0}".format(side),
                                  toe="toe.{0}".format(side))


class RigifyCtrlsBase(HumanSkeleton):
    def __init__(self):
        self.face = SimpleFace(
            jaw='',
            left_eye='eye_master.L',
            right_eye='eye_master.R'
        )

        self.spine = HumanSpine(
            head='head',
            neck='neck',
            spine2='spine_fk.003',
            spine1='spine_fk.002',
            spine='spine_fk.001',
            hips='torso'
        )
        self.root = 'root'

        side = 'L'
        self.left_fingers = HumanFingers(
            thumb=["thumb.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            index=["f_index.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            middle=["f_middle.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            ring=["f_ring.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            pinky=["f_pinky.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
        )

        side = 'R'
        self.right_fingers = HumanFingers(
            thumb=["thumb.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            index=["f_index.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            middle=["f_middle.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            ring=["f_ring.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
            pinky=["f_pinky.{1:02d}.{0}".format(side, i) for i in range(1, 4)],
        )

    @property
    def deformation_bone_map(self):
        return self.conversion_map(RigifySkeleton())


class RigifyCtrls(RigifyCtrlsBase):
    def __init__(self):
        super().__init__()

        side = 'L'
        self.left_arm = HumanArm(shoulder="shoulder.{0}".format(side),
                                 arm="upper_arm_fk.{0}".format(side),
                                 forearm="forearm_fk.{0}".format(side),
                                 hand="hand_fk.{0}".format(side))

        self.left_leg = HumanLeg(upleg="thigh_fk.{0}".format(side),
                                 leg="shin_fk.{0}".format(side),
                                 foot="foot_fk.{0}".format(side),
                                 toe="toe.{0}".format(side))

        self.left_arm_ik = HumanArm(shoulder="shoulder.{0}".format(side),
                                 arm="upper_arm_ik.{0}".format(side),
                                 hand="hand_ik.{0}".format(side))

        self.left_leg_ik = HumanLeg(upleg="thigh_ik.{0}".format(side),
                                 foot="foot_ik.{0}".format(side),
                                 toe="toe.{0}".format(side))

        side = 'R'
        self.right_arm = HumanArm(shoulder="shoulder.{0}".format(side),
                                  arm="upper_arm_fk.{0}".format(side),
                                  forearm="forearm_fk.{0}".format(side),
                                  hand="hand_fk.{0}".format(side))

        self.right_leg = HumanLeg(upleg="thigh_fk.{0}".format(side),
                                  leg="shin_fk.{0}".format(side),
                                  foot="foot_fk.{0}".format(side),
                                  toe="toe.{0}".format(side))

        self.right_arm_ik = HumanArm(shoulder="shoulder.{0}".format(side),
                                  arm="upper_arm_ik.{0}".format(side),
                                  hand="hand_ik.{0}".format(side))

        self.right_leg_ik = HumanLeg(upleg="thigh_ik.{0}".format(side),
                                  foot="foot_ik.{0}".format(side),
                                  toe="toe.{0}".format(side))


class UnrealSkeleton(HumanSkeleton):
    def __init__(self):
        self.spine = HumanSpine(
            head='head',
            neck='neck_01',
            spine2='spine_03',
            spine1='spine_02',
            spine='spine_01',
            hips='pelvis'
        )

        for side, side_letter in zip(('left', 'right'), ('_l', '_r')):
            arm = HumanArm(shoulder="clavicle" + side_letter,
                           arm="upperarm" + side_letter,
                           forearm="lowerarm" + side_letter,
                           hand="hand" + side_letter)

            arm.arm_twist = "upperarm_twist_01" + side_letter
            arm.forearm_twist = "lowerarm_twist_01" + side_letter
            setattr(self, side + "_arm", arm)

            fingers = HumanFingers(
                    thumb=["thumb_{0:02d}{1}".format(i, side_letter) for i in range(1, 4)],
                    index=["index_{0:02d}{1}".format(i, side_letter) for i in range(1, 4)],
                    middle=["middle_{0:02d}{1}".format(i, side_letter) for i in range(1, 4)],
                    ring=["ring_{0:02d}{1}".format(i, side_letter) for i in range(1, 4)],
                    pinky=["pinky_{0:02d}{1}".format(i, side_letter) for i in range(1, 4)],
                )
            setattr(self, side + "_fingers", fingers)

            leg = HumanLeg(upleg="thigh{0}".format(side_letter),
                           leg="calf{0}".format(side_letter),
                           foot="foot{0}".format(side_letter),
                           toe="ball{0}".format(side_letter))

            leg.upleg_twist = "thigh_twist_01" + side_letter
            leg.leg_twist = "calf_twist_01" + side_letter
            setattr(self, side + "_leg", leg)


def get_rigify_version():
    global rigify_version
    try:
        from rigify import bl_info as rigify_bl_info
        rigify_version = rigify_bl_info.get("version")
    except:
        rigify_version = None
    return rigify_version

get_rigify_version()

# test
if __name__ == "__main__":
    rigify = RigifySkeleton()
    bone_map = rigify.conversion_map(MixamoSkeleton())

    print("Bone Map:")
    for k, v in bone_map.items():
        print('\t', k, v)
