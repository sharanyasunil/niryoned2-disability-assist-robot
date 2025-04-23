from pyniryo import *
import time

# Connect to robot
robot = NiryoRobot("10.10.10.10")  # Replace with your robot's IP

# Setup
robot.calibrate_auto()
robot.update_tool()
robot.move_joints([0.097, -0.263, -0.889, 0.193, 1.114, -0.054])

# Define tasks
task_times = {
    "pour": [1, 0, 0,0],
    "lid":  [0, 1, 0,0],
    "feed": [0, 0, 1,0],
    "zip": [0, 0, 0,1]
}

t1, t2, t3, t4 = task_times[input("Enter task (pour / lid / feed / zip): ").strip().lower()]
print("Selected task timings:", t1, t2, t3, t4)

# === Task 1: Pour Water ===
if t1:
    print("Starting POUR task...", flush=True)
    robot.open_gripper()

    # Bottle pickup
    robot.move_joints([0.1, -0.75, -0.65, 0.1, 1.25, 0.02])
    robot.close_gripper()
    time.sleep(1)

    # Move to above cup
    robot.move_joints([0.1, -0.3, -0.85, 0.15, 1.1, -0.05])

    # Tilt down to simulate pouring
    robot.move_joints([0.1, -0.3, -0.85, 0.80, 1.1, 0.6])  # Wrist rotated
    time.sleep(2)

    # Tilt back up
    robot.move_joints([0.1, -0.3, -0.85, 0.15, 1.1, -0.05])

    # Return and place back
    robot.move_joints([0.1, -0.75, -0.65, 0.1, 1.25, 0.02])
    robot.open_gripper()

    # Return to center
    robot.move_joints([0.097, -0.263, -0.889, 0.193, 1.114, -0.054])

# === Task 2: Place Lid ===
if t2:
    print("Starting LID PLACEMENT task...", flush=True)
    robot.open_gripper()

    # Lid pickup
    robot.move_joints([-0.4, -0.3, -0.8, -0.5, 1.0, 0.18])
    robot.close_gripper()
    time.sleep(1)

    # Move above cup and place lid
    robot.move_joints([0.1, -0.4, -0.95, 0.0, 1.4, 0.0])
    time.sleep(1)
    robot.open_gripper()

    # Return
    #robot.move_joints([-0.4, -0.3, -0.8, -0.5, 1.0, 0.18])
    robot.move_joints([0.097, -0.263, -0.889, 0.193, 1.114, -0.054])

# === Task 3: Feed Food ===
if t3:
    print("Starting FEEDING task...", flush=True)
    robot.open_gripper()

    # Step 1: Move to side of spoon, slightly above (no lowering yet)
    robot.move_joints([0.9, -0.55, -0.4, 1.2, 1.35, 1.57])  # Approaching side
    time.sleep(1)

    # Step 2: Lower arm and move slightly forward to scoop spoon
    robot.move_joints([0.92, -0.8, -0.5, 1.2, 1.35, 1.57])  # Lower + move in
    time.sleep(1)
    robot.close_gripper()
    time.sleep(1)

    # Step 3: Lift slightly with spoon in hand
    robot.move_joints([0.9, -0.6, -0.45, 0.9, 1.35, 1.57])
    time.sleep(1)

    # Step 4: Move to mouth/feeding position
    robot.move_joints([0.4, -0.2, -0.7, 0.5, 1.1, 1.57])
    time.sleep(2)

    # Step 5: Return to original bowl position (but do not drop spoon yet)
    robot.move_joints([0.92, -0.7, -0.5, 1.2, 1.35, 1.57])  # Lower + move in
    time.sleep(1)
   
    # Step 6: Release spoon
    robot.open_gripper()
    time.sleep(1)

    # Step 7: Raise arm slightly after drop
    robot.move_joints([0.9, -0.4, -0.3, 0.9, 1.2, 1.57])  # Lift back up
    time.sleep(1)

    # Step 8: Return to rest position
    robot.move_joints([0.097, -0.263, -0.889, 0.193, 1.114, -0.054])
# === Task 4: Fasten Zipper ===
if t4:
    print("Starting ZIPPER task...", flush=True)

    # Move to zipper start position
    robot.open_gripper(400)
    robot.move_joints(0.1, -0.4, -0.75, 0.0, 1.4, 1.57)  # adjust to start of zipper
    time.sleep(1)
    robot.close_gripper(600)  # hold zipper tab
    time.sleep(1)

    # Move along zipper line (simulate zipping up)
    robot.move_joints(0.1, -0.3, -0.75, 0.0, 1.3, 1.57)  # mid-point
    time.sleep(1)
    robot.move_joints(0.1, -0.2, -0.75, 0.0, 1.2, 1.57)    # end of zipper line
    time.sleep(1)

    # Release zipper
    robot.open_gripper(400)
    time.sleep(1)

    # Return to rest
    #robot.move_joints(0.5, -0.6, -0.8, 0.0, 1.4, 1.57)
    robot.move_joints(0.097, -0.263, -0.889, 0.193, 1.114, -0.054)

# Disconnect
robot.close_connection()
