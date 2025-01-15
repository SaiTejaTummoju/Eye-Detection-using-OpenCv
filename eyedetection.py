import os
import cv2

# Initialize video capture
cap = cv2.VideoCapture(0)

# Load the Haar Cascade for eye detection
path = cv2.data.haarcascades + 'haarcascade_eye.xml'
eye_cascade = cv2.CascadeClassifier(path)

if not eye_cascade.empty():
    print("Cascade classifier loaded successfully.")
else:
    print("Error loading cascade classifier.")

frame_count = 0  # Counter to process every nth frame

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize frame to a smaller size for faster processing
    frame = cv2.resize(frame, (320, 240))

    # Convert to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Process every 2nd frame to reduce lag
    if frame_count % 2 == 0:
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))
    else:
        eyes = []  # Skip processing

    frame_count += 1

    # Draw circles around the detected eyes
    for (x, y, w, h) in eyes:
        xc = (x + x + w) // 2
        yc = (y + y + h) // 2
        radius = w // 2
        cv2.circle(frame, (xc, yc), radius, (255, 0, 0), 2)

    # Display the frame with eye detection
    cv2.imshow("Frame", frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
