# Capstone Proposal

## Project Title: USafe 

### Group Members:

- Nada Almutairi
- Refal Alboqami
- Dalal Alharbi

### USafe Demo:

<img  src="Demo.jpeg" hight=100 width=100  >

https://scanned.page/p/658b54f859151

### Main Objective:

The main objective of the USafe project is to develop a device capable of detecting cases of fainting using a camera and alerting the surrounding individuals by triggering an alarm bell.

### Subobjectives:

- Develop a deep learning model for automatic detection of fainting cases by analyzing the video stream from the camera.
- Improve the accuracy of fainting detection by training the model on a wide range of possible fainting scenarios.
- Design and develop an alarm bell activation system that is automatically triggered upon detecting a fainting case.
- Test and evaluate the performance of the system using a diverse set of data and scenarios.


### Dataset Link:

https://drive.google.com/drive/folders/1xt64LjVIvjJVanxZRNy66j2-TIej51jN?usp=sharing


### The Expected (Machine Learning / Deep Learning) Algorithms:

- Deep Learning: We utilized deep learning techniques to develop our fainting cases detection system.
YOLOv8: We employed the YOLOv8 model, which is a cutting-edge object detection algorithm, for detecting fainting instances. YOLOv8 is known for its real-time object detection capabilities.

- OpenCV: OpenCV, an open-source computer vision library, was utilized in conjunction with YOLOv8 for image and video analysis tasks in our system.

- Deployment with Django: We deployed our model using the Django framework. Django facilitated the creation of a user-friendly web interface, enabling seamless interaction with the system.

- Customized Training: We meticulously customized and fine-tuned the YOLOv8 model to achieve high accuracy and robustness in detecting fainting cases across various environments.

### Key Contributions:
-	Developed a custom YOLOv8 model for fainting detection.
-	Integrated the model into a web application using Django framework.
-	Implemented real-time alerts upon detection of fainting instances.
-	Ensured user-friendly interface and smooth functionality.
