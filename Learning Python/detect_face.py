import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
st.title("Webcam📹 Face👩 Detection ")
FRAME_WINDOW = st.image([])
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return frame

# Using OpenCV to capture from device 0. If you have trouble capturing
# from a webcam, comment the line below out and use a video file
# instead.
cap = cv2.VideoCapture(0)
#st.cache()

st.title('Face Detection using OpenCV')
st.code("""import cv2
import streamlit as st

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
st.title("Webcam Face Detection")
FRAME_WINDOW = st.image([])
def detect_faces(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return frame

# Using OpenCV to capture from device 0. If you have trouble capturing
# from a webcam, comment the line below out and use a video file
# instead.
cap = cv2.VideoCapture(0)
#st.cache()

st.title('Face Detection using OpenCV')

while True:
    ret, frame = cap.read()
    if ret:
        frame = detect_faces(frame)
        #st.title("Webcam Face Recognition")
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), use_column_width=True)
    else:
        st.warning('Unable to capture video')
        break

cap.release()
cv2.destroyAllWindows()
""")
st.success("""The code above uses OpenCV, a computer vision library, and streamlit, a Python library for building interactive web-based applications, to perform face detection on a live video feed from a webcam.

At the beginning, the haarcascade_frontalface_default.xml file is loaded as a classifier for face detection using cv2.CascadeClassifier. Then, the streamlit title is set to "Webcam Face Detection" and an empty image widget is created with st.image.

The detect_faces function takes a frame (image) as an input and converts it to grayscale using cv2.cvtColor and cv2.COLOR_BGR2GRAY. Then, it uses the face_cascade classifier to detect faces in the image using face_cascade.detectMultiScale. For each face detected, a rectangle is drawn around it using cv2.rectangle. Finally, the modified frame with rectangles around faces is returned.

The code then opens a video capture using cv2.VideoCapture(0) to start capturing frames from the webcam. In the while loop, it continually reads frames from the video capture using cap.read(). If a frame is successfully read, it is passed to the detect_faces function, and the result is displayed in the image widget using FRAME_WINDOW.image. If a frame cannot be captured, a warning message "Unable to capture video" is displayed.

After the loop ends, the video capture is released using cap.release() and all windows are destroyed using cv2.destroyAllWindows().""")

while True:
    ret, frame = cap.read()
    if ret:
        frame = detect_faces(frame)
        #st.title("Webcam Face Recognition")
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), use_column_width=True)
    else:
        st.warning('Unable to capture video')
        break

cap.release()
cv2.destroyAllWindows()
