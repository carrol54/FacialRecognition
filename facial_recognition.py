import face_recognition
from tkinter import *
from tkinter import filedialog
from PIL import Image
import cv2
import sys

#Loads the image and returns the image variable
def load_image(image_loc):
  image = face_recognition.load_image_file(image_loc)
  return image

#Returns an array of all face locations
def get_faces(image):
  face_locations = face_recognition.face_locations(image)
  return face_locations

#Tells where all faces are found and shows images
def map_faces(face_locations, image):
    for face_location in face_locations:
        top, right, bottom, left = face_location
        print("A face was located at {}, {}, {}, {}".format(top, left, bottom, right))
        #Shows the images
        face = image[top:bottom, left:right]
        pil_image = Image.fromarray(face)
        pil_image.show()

#Opens a file dialog box to pick the image file
def getImageFile():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select an image",
                                          filetypes = (("Jpeg files",
                                                        "*.jpg"),
                                                        ("All files",
                                                         "*.*")))
    image = load_image(filename)
    map_faces(get_faces(image), image)

def createGraphic():
    window = Tk()
    window.title("Facial Recognition")
    window.geometry("500x200")
    window.config(background="white")
    label_find_file = Label(window,
                            text = "Select image file",
                            width = 100, height = 5,
                            fg = "black")
    button_file = Button(window,
                         text = "Select file",
                         command = getImageFile)
    button_webcam = Button(window,
                         text = "Use Webcam (press 'q' to quit)",
                         command = webcam)
    button_exit = Button(window,
                         text = "Exit",
                         command = exit)
    label_find_file.pack()
    button_file.pack()
    button_webcam.pack()
    button_exit.pack()
    window.mainloop()

def getFile():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select an image",
                                          filetypes = (("Jpeg files",
                                                        "*.jpg"),
                                                        ("All files",
                                                         "*.*")))
    return filename

def webcam():
    video_capture = cv2.VideoCapture(0)

    # Initialize variables
    face_locations = []

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame)

        # Display the results
        for top, right, bottom, left in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

createGraphic()
