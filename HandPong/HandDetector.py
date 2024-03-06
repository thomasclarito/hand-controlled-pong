import cv2
import mediapipe as mp
import os

from .constants import WINDOW_HEIGHT
from .constants import WINDOW_WIDTH
from .Cursor import Cursor

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
model_path = os.path.abspath("./models/gesture_recognizer.task")


class HandDetector:
    def __init__(self):
        options = GestureRecognizerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.IMAGE,
            num_hands=1,
        )
        # Create a VideoCapture object to access the webcam
        self.cap = cv2.VideoCapture(0)
        # Create a detector for gestures and hand landmarks
        self.detector = GestureRecognizer.create_from_options(options)

    def get_pointer_location(self, cursor: Cursor) -> Cursor:
        """Get the location of the index finger tip."""

        # Read the current frame from the webcam
        ret, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        result = self.detector.recognize(mp_image)

        # Detect the frame with the hand tracking module
        if result.hand_landmarks:
            index_tip = result.hand_landmarks[0][
                mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP
            ]
            # Update the cursor location to the location of the index finger
            cursor.posx = int(index_tip.x * WINDOW_WIDTH)
            cursor.posy = int(index_tip.y * WINDOW_HEIGHT)

        return cursor

    def check_gesture(self) -> bool:
        """Check if the user is making a thumbs up gesture for 20 consecutive frames."""
        for i in range(20):
            # Read the current frame from the webcam

            ret, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB, data=frame_rgb
            )
            result = self.detector.recognize(mp_image)

            if result.gestures:
                if result.gestures[0][0].category_name == "Thumb_Up":
                    continue

            return False

        return True

    def cleanup(self):
        # Release the VideoCapture object
        self.cap.release()
