import cv2 as cv
  


def rescaleFrame(frame, scale=0.75): #risized frame by scale (set to 0.75 or 75%). *Images, Videos and Live Videos*
   width = int(frame.shape[1] * scale)
   height = int(frame.shape[0] * scale)
   dimensions = (width, height)
   return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) 

def changeRes(width, height): #changes resolution *LIVE VIDEO ONLY*
   capture.set(3, width)
   capture.set(4, height)




#                                ********reading videos********

# defines a video capture object. 0 for webcam, path fir video
capture = cv.VideoCapture(0)
  
while(True):
      
    # Captures  video frame by frame
    istrue, frame = capture.read() 
  
    frame_resized = rescaleFrame(frame, scale=0.75) #resizes the frame 

    gray = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY) #converts the frame to gray scale. necessary for haar cascade to work

    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7) #minNeighbors parameter determines accuracy of the detection. Higher value means less accuracy but more faces detected
    
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame_resized, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    
    cv.imshow('Detected faces', frame_resized) #displays the frame with the detected faces


    if cv.waitKey(1) & 0xFF == ord('b'): #if 'b' key is pressed, break out of loop and close all windows
        break
  
capture.release()# releases video capture
cv.destroyAllWindows()# Destroy all  windows