# Import libraries
import cv2 # type: ignore
from ultralytics import YOLO #type: ignore

# Load YOLOv8 pre-trained model
model = YOLO("yolov8n.pt")  # Nano model (downloads automatically)

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    # Read frame from webcam
    success, frame = cap.read()

    if not success:
        break

    # Detect and Track Objects
    results = model.track(
        frame,
        persist=True,     # Keep tracking IDs
        conf=0.5          # Confidence threshold
    )

    # Draw bounding boxes and tracking IDs
    annotated_frame = results[0].plot()

    # Display output
    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
