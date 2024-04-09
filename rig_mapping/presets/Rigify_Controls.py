import bpy
skeleton = bpy.context.object.data.expykit_retarget

skeleton.face.jaw = 'jaw_master'
skeleton.face.left_eye = 'eye_master.L'
skeleton.face.right_eye = 'eye_master.R'

skeleton.spine.head = 'head'
skeleton.spine.neck = 'neck'
skeleton.spine.spine2 = 'spine_fk.003'
skeleton.spine.spine1 = 'spine_fk.002'
skeleton.spine.spine = 'spine_fk.001'
skeleton.spine.hips = 'torso'

skeleton.right_arm.shoulder = 'shoulder.R'
skeleton.right_arm.arm = 'upper_arm_fk.R'
skeleton.right_arm.arm_twist = 'upper_arm_tweak.R.001'
skeleton.right_arm.forearm = 'forearm_fk.R'
skeleton.right_arm.forearm_twist = 'forearm_tweak.R.001'
skeleton.right_arm.hand = 'hand_fk.R'

skeleton.left_arm.shoulder = 'shoulder.L'
skeleton.left_arm.arm = 'upper_arm_fk.L'
skeleton.left_arm.arm_twist = 'upper_arm_tweak.L.001'
skeleton.left_arm.forearm = 'forearm_fk.L'
skeleton.left_arm.forearm_twist = 'forearm_tweak.L.001'
skeleton.left_arm.hand = 'hand_fk.L'

skeleton.right_leg.upleg = 'thigh_fk.R'
skeleton.right_leg.upleg_twist = 'thigh_tweak.R.001'
skeleton.right_leg.leg = 'shin_fk.R'
skeleton.right_leg.leg_twist = 'shin_tweak.R.001'
skeleton.right_leg.foot = 'foot_fk.R'
skeleton.right_leg.toe = 'toe.R'

skeleton.left_leg.upleg = 'thigh_fk.L'
skeleton.left_leg.upleg_twist = 'thigh_tweak.L.001'
skeleton.left_leg.leg = 'shin_fk.L'
skeleton.left_leg.leg_twist = 'shin_tweak.L.001'
skeleton.left_leg.foot = 'foot_fk.L'
skeleton.left_leg.toe = 'toe.L'

skeleton.right_fingers.thumb.a = 'thumb.01.R'
skeleton.right_fingers.thumb.b = 'thumb.02.R'
skeleton.right_fingers.thumb.c = 'thumb.03.R'

skeleton.right_fingers.index.a = 'f_index.01.R'
skeleton.right_fingers.index.b = 'f_index.02.R'
skeleton.right_fingers.index.c = 'f_index.03.R'

skeleton.right_fingers.middle.a = 'f_middle.01.R'
skeleton.right_fingers.middle.b = 'f_middle.02.R'
skeleton.right_fingers.middle.c = 'f_middle.03.R'

skeleton.right_fingers.ring.a = 'f_ring.01.R'
skeleton.right_fingers.ring.b = 'f_ring.02.R'
skeleton.right_fingers.ring.c = 'f_ring.03.R'

skeleton.right_fingers.pinky.a = 'f_pinky.01.R'
skeleton.right_fingers.pinky.b = 'f_pinky.02.R'
skeleton.right_fingers.pinky.c = 'f_pinky.03.R'

skeleton.left_fingers.thumb.a = 'thumb.01.L'
skeleton.left_fingers.thumb.b = 'thumb.02.L'
skeleton.left_fingers.thumb.c = 'thumb.03.L'

skeleton.left_fingers.index.a = 'f_index.01.L'
skeleton.left_fingers.index.b = 'f_index.02.L'
skeleton.left_fingers.index.c = 'f_index.03.L'

skeleton.left_fingers.middle.a = 'f_middle.01.L'
skeleton.left_fingers.middle.b = 'f_middle.02.L'
skeleton.left_fingers.middle.c = 'f_middle.03.L'

skeleton.left_fingers.ring.a = 'f_ring.01.L'
skeleton.left_fingers.ring.b = 'f_ring.02.L'
skeleton.left_fingers.ring.c = 'f_ring.03.L'

skeleton.left_fingers.pinky.a = 'f_pinky.01.L'
skeleton.left_fingers.pinky.b = 'f_pinky.02.L'
skeleton.left_fingers.pinky.c = 'f_pinky.03.L'

skeleton.right_arm_ik.shoulder = 'shoulder.R'
skeleton.right_arm_ik.arm = 'upper_arm_ik.R'
skeleton.right_arm_ik.arm_twist = 'upper_arm_tweak.R.001'
skeleton.right_arm_ik.forearm = ''
skeleton.right_arm_ik.forearm_twist = 'forearm_tweak.R.001'
skeleton.right_arm_ik.hand = 'hand_ik.R'

skeleton.left_arm_ik.shoulder = 'shoulder.L'
skeleton.left_arm_ik.arm = 'upper_arm_ik.L'
skeleton.left_arm_ik.arm_twist = 'upper_arm_tweak.L.001'
skeleton.left_arm_ik.forearm = ''
skeleton.left_arm_ik.forearm_twist = 'forearm_tweak.L.001'
skeleton.left_arm_ik.hand = 'hand_ik.L'

skeleton.right_leg_ik.upleg = 'thigh_ik.R'
skeleton.right_leg_ik.upleg_twist = 'thigh_tweak.R.001'
skeleton.right_leg_ik.leg = ''
skeleton.right_leg_ik.leg_twist = 'shin_tweak.R.001'
skeleton.right_leg_ik.foot = 'foot_ik.R'
skeleton.right_leg_ik.toe = 'toe.R'

skeleton.left_leg_ik.upleg = 'thigh_ik.L'
skeleton.left_leg_ik.upleg_twist = 'thigh_tweak.L.001'
skeleton.left_leg_ik.leg = ''
skeleton.left_leg_ik.leg_twist = 'shin_tweak.L.001'
skeleton.left_leg_ik.foot = 'foot_ik.L'
skeleton.left_leg_ik.toe = 'toe.L'

skeleton.root = 'root'

skeleton.deform_preset = 'Rigify_Deform.py'
