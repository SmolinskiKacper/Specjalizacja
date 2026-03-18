import pathlib
import cv2

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf = cv2.CascadeClassifier(str(cascade_path))
# video = cv2.VideoCapture("man.mp4")
camera = cv2.VideoCapture(0)

paused = False
cv2.namedWindow("Faces")

while True:
    if cv2.getWindowProperty("Faces", cv2.WND_PROP_VISIBLE) < 1:
        break

    if not paused:
        ret, frame = camera.read()

        if not ret:
            print("Video ended or failed to read frame.")
            break

        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = clf.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            for (x, y, width, height) in faces:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)

            cv2.imshow("Faces", frame)
            last_frame = frame

        except Exception as e:
            print(f"Error processing frame: {e}")
            break

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("p"):
        paused = not paused
        print("Paused" if paused else "Resumed")

camera.release()
cv2.destroyAllWindows()