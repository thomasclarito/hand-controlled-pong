import cv2
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
import os

from constants import WINDOW_HEIGHT
from constants import WINDOW_WIDTH
from Cursor import Cursor

HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
BaseOptions = mp.tasks.BaseOptions
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
model_path = os.path.abspath("./models/hand_landmarker.task")


class HandDetector:
    def __init__(self):
        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.IMAGE,
            num_hands=1,
        )

        # Create a VideoCapture object to access the webcam
        self.cap = cv2.VideoCapture(0)
        # Create a hand tracking module
        # self.mp_hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.landmarker = HandLandmarker.create_from_options(options)

    def get_pointer_location(self, cursor: Cursor) -> Cursor:
        """Get the location of the index finger tip."""

        # Read the current frame from the webcam
        ret, frame = self.cap.read()

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        result = self.landmarker.detect(mp_image)
        # Detect the frame with the hand tracking module
        if result.hand_landmarks:
            index_tip = result.hand_landmarks[0][
                mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP
            ]
            # hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            # hand_landmarks_proto.landmark.extend([
            # landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in result.hand_landmarks[0]
            # ])
            # # Draw the hand landmarks on the frame
            # mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks_proto, mp.solutions.hands.HAND_CONNECTIONS)

            cursor.posx = int(index_tip.x * WINDOW_WIDTH)
            cursor.posy = int(index_tip.y * WINDOW_HEIGHT)

        
        # cv2.imshow("Hand Tracking", frame)
        # cv2.waitKey(1)
        return cursor


    def cleanup(self):
        # Release the VideoCapture object
        self.cap.release()


# TODO: Create a new cursor class that tracks the index finger tip and displays it on the screen

# Create an instance of the HandDetector class and run it
# hand_detector = HandDetector()
# while True:
#     hand_detector.get_pointer_location()
