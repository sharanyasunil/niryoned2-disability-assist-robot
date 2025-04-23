# 🤖 Disability Assistance with Niryo NED2

This project implements a set of real-world assistive tasks using the Niryo NED2 6-DOF robotic arm, built for the Mobile and Autonomous Robots course. The robot is programmed to assist in everyday tasks like:

- Pouring water into a cup
- Placing a lid on a cup
- Feeding food with a spoon
- Fastening a zipper

Each task was performed through hardware execution using the `pyniryo` Python API, with safe joint configurations and dynamic grip control.

---

## 📁 Project Structure

- `main.py`: Unified script to run the task


---

## 🧠 How It Works

- Calibrates the robot using Niryo Studio
- Uses `pyniryo` API to send joint and pose commands
- Each task uses pre-defined joint angles and grip strengths
- Wrist rotation and pitch are adjusted per task to maintain object alignment

---

## 💻 Software Used

- Niryo Studio
- Python 3.10+
- `pyniryo` Python package
- ROS2 Humble + Gazebo (for simulation attempts)

---

## 🛠️ Hardware Components

- Niryo NED2 6-DOF robotic arm
- Standard gripper
- Spoon, lid, cup, and zipper cloth

---

## 📈 Outcomes

- ✅ Smooth motion for all 4 assistive tasks
- ✅ Pose-based zipper motion using Cartesian planning
- ✅ Feeding task included natural wrist pitch and center alignment
- ✅ Simulation tested in ROS2 Humble and Gazebo

---

## 🎥 Demo Video

📽️ https://drive.google.com/drive/folders/1gNqzkpp8bpvemPDN9ubpL_VUx9D0m_H6?usp=sharing


---

## 🔗 References

- [Niryo Documentation](https://niryo.com/docs/)
- [ROS2 Humble Tutorials](https://docs.ros.org/en/humble/index.html)
- [Gazebo Tutorials](https://gazebosim.org/tutorials)

---


