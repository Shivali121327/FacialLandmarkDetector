import dlib,cv2
import numpy as np
from renderFace import renderFace

def writeLandmarksToFile(landmarks, landmarksFileName):
  with open(landmarksFileName, 'w') as f:
    for p in landmarks.parts():
      f.write("%s %s\n" %(int(p.x),int(p.y)))

  f.close()

# Landmark model location
PREDICTOR_PATH = "./data/models/shape_predictor_68_face_landmarks.dat"
# Get the face detector
faceDetector = dlib.get_frontal_face_detector()
# The landmark detector is implemented in the shape_predictor class
landmarkDetector = dlib.shape_predictor(PREDICTOR_PATH)

# Read image
imageFilename = "./data/images/family.jpg"
im= cv2.imread(imageFilename)
imDlib = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
# landmarks will be stored in results/family_i.txt
landmarksBasename = "results/family"

# Detect faces in the image
faceRects = faceDetector(imDlib, 0)
print("Number of faces detected: ",len(faceRects))

# List to store landmarks of all detected faces
landmarksAll = []

# Loop over all detected face rectangles
for i in range(0, len(faceRects)):
  newRect = dlib.rectangle(int(faceRects[i].left()),int(faceRects[i].top()),
      int(faceRects[i].right()),int(faceRects[i].bottom()))

  # For every face rectangle, run landmarkDetector
  landmarks = landmarkDetector(imDlib, newRect)
  # Print number of landmarks
  if i==0:
    print("Number of landmarks",len(landmarks.parts()))

  # Store landmarks for current face
  landmarksAll.append(landmarks)
  # Draw landmarks on face
  renderFace(im, landmarks)

  landmarksFileName = landmarksBasename +"_"+ str(i)+ ".txt"
  print("Saving landmarks to", landmarksFileName)
  # Write landmarks to disk
  writeLandmarksToFile(landmarks, landmarksFileName)

outputFileName = "results/familyLandmarks.jpg"
print("Saving output image to", outputFileName)
cv2.imwrite(outputFileName, im)

cv2.imshow("Facial Landmark detector", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
