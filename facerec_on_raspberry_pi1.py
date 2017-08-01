
import face_recognition
import picamera
import numpy as np
import os

camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

print("Loading known face image(s)")
ep_image = face_recognition.load_image_file("/home/pi/Documents/pic/ep.jpg")
ep_face_encoding = face_recognition.face_encodings(ep_image)[0]
vl_image = face_recognition.load_image_file("/home/pi/Documents/pic/vl.jpg")
vl_face_encoding = face_recognition.face_encodings(vl_image)[0]

face_locations = []
face_encodings = []

while True:
    print("Capturing image.")
    camera.capture(output, format="rgb")

    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces([ep_face_encoding,vl_face_encoding], face_encoding)
        name = "<Unknown Person>"
        os.system("python /home/pi/led2.py &")
        import time
        date_string = time.strftime("%Y-%m-%d-%H:%M:%S")
        camera.capture("/home/pi/Documents/unknown/image-" + date_string + ".jpg")

        if match[0]:
            name = "Evghenii"
            os.system("fbi -T 1 -d /dev/fb1 -noverbose /home/pi/Documents/pic/ep.jpg")
            os.system("sh /home/pi/Documents/open.sh")
            os.system("sleep 2")
            os.system("killall fbi")

        if match[1]:
            name = "Vlad"
            os.system("fbi -T 1 -d /dev/fb1 -noverbose /home/pi/Documents/pic/vl.jpg")
            os.system("sh /home/pi/Documents/open.sh")
            os.system("sleep 2")
            os.system("killall fbi")

        print("I see someone named {}!".format(name))
