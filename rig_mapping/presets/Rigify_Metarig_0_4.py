import bpy
skeleton = bpy.context.object.data.expykit_retarget

skeleton.face.super_copy = False

skeleton.spine.head = 'head'
skeleton.spine.neck = 'neck'
skeleton.spine.spine2 = 'chest'
skeleton.spine.spine = 'spine'
skeleton.spine.hips = 'hips'

skeleton.right_arm.shoulder = 'shoulder.R'
skeleton.right_arm.arm = 'upper_arm.R'
skeleton.right_arm.forearm = 'forearm.R'
skeleton.right_arm.hand = 'hand.R'

skeleton.left_arm.shoulder = 'shoulder.L'
skeleton.left_arm.arm = 'upper_arm.L'
skeleton.left_arm.forearm = 'forearm.L'
skeleton.left_arm.hand = 'hand.L'

skeleton.right_leg.upleg = 'thigh.R'
skeleton.right_leg.leg = 'shin.R'
skeleton.right_leg.foot = 'foot.R'
skeleton.right_leg.toe = 'toe.R'

skeleton.left_leg.upleg = 'thigh.L'
skeleton.left_leg.leg = 'shin.L'
skeleton.left_leg.foot = 'foot.L'
skeleton.left_leg.toe = 'toe.L'

skeleton.left_fingers.thumb.a = 'thumb.01.L'
skeleton.left_fingers.thumb.b = 'thumb.02.L'
skeleton.left_fingers.thumb.c = 'thumb.03.L'

skeleton.left_fingers.index.meta = 'palm.01.L'
skeleton.left_fingers.index.a = 'f_index.01.L'
skeleton.left_fingers.index.b = 'f_index.02.L'
skeleton.left_fingers.index.c = 'f_index.03.L'

skeleton.left_fingers.middle.meta = 'palm.02.L'
skeleton.left_fingers.middle.a = 'f_middle.01.L'
skeleton.left_fingers.middle.b = 'f_middle.02.L'
skeleton.left_fingers.middle.c = 'f_middle.03.L'

skeleton.left_fingers.ring.meta = 'palm.03.L'
skeleton.left_fingers.ring.a = 'f_ring.01.L'
skeleton.left_fingers.ring.b = 'f_ring.02.L'
skeleton.left_fingers.ring.c = 'f_ring.03.L'

skeleton.left_fingers.pinky.meta = 'palm.04.L'
skeleton.left_fingers.pinky.a = 'f_pinky.01.L'
skeleton.left_fingers.pinky.b = 'f_pinky.02.L'
skeleton.left_fingers.pinky.c = 'f_pinky.03.L'

skeleton.right_fingers.thumb.a = 'thumb.01.R'
skeleton.right_fingers.thumb.b = 'thumb.02.R'
skeleton.right_fingers.thumb.c = 'thumb.03.R'

skeleton.right_fingers.index.meta = 'palm.01.R'
skeleton.right_fingers.index.a = 'f_index.01.R'
skeleton.right_fingers.index.b = 'f_index.02.R'
skeleton.right_fingers.index.c = 'f_index.03.R'

skeleton.right_fingers.middle.meta = 'palm.02.R'
skeleton.right_fingers.middle.a = 'f_middle.01.R'
skeleton.right_fingers.middle.b = 'f_middle.02.R'
skeleton.right_fingers.middle.c = 'f_middle.03.R'

skeleton.right_fingers.ring.meta = 'palm.03.R'
skeleton.right_fingers.ring.a = 'f_ring.01.R'
skeleton.right_fingers.ring.b = 'f_ring.02.R'
skeleton.right_fingers.ring.c = 'f_ring.03.R'

skeleton.right_fingers.pinky.meta = 'palm.04.R'
skeleton.right_fingers.pinky.a = 'f_pinky.01.R'
skeleton.right_fingers.pinky.b = 'f_pinky.02.R'
skeleton.right_fingers.pinky.c = 'f_pinky.03.R'

skeleton.deform_preset = '--'
