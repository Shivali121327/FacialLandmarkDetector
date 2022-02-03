# FacialLandmarkDetector
Facial Landmark Detection Using Dlib

Landmark detection is a two step process:

In the first step, we need to detect the face in an image. For best results we should use the same face detector used in training the landmark detector. The output of a face detector is a rectangle (x, y, w, h) that contains the face. Dlib’s face detector is based on Histogram of Oriented Gradients features and Support Vector Machines (SVM).

In the second step, The landmark detector finds the landmark points inside the face rectangle.
