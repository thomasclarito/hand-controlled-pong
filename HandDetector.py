import cv2
import mediapipe as mp

from constants import WINDOW_HEIGHT
from constants import WINDOW_WIDTH
from Cursor import Cursor


class HandDetector:
    def __init__(self):
        # Create a VideoCapture object to access the webcam
        self.cap = cv2.VideoCapture(0)
        # Create a hand tracking module
        self.mp_hands = mp.solutions.hands.Hands(max_num_hands=1)

    def get_pointer_location(self, cursor: Cursor) -> Cursor:
        """Get the location of the index finger tip."""

        # Read the current frame from the webcam
        ret, frame = self.cap.read()

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with the hand tracking module
        results = self.mp_hands.process(frame_rgb)

        # Check if any hands are detected
        if results.multi_hand_landmarks:
            # handedness = results.multi_handedness[0]
            # classification = handedness.classification[0]
            # if classification.label == "Right":
            hand_landmarks = results.multi_hand_landmarks[0]
            index_tip = hand_landmarks.landmark[
                mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP
            ]
            # Draw the hand landmarks on the frame
            # mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            # Display the frame with the hand landmarks
            cursor.posx = int(index_tip.x * WINDOW_WIDTH)
            cursor.posy = int(index_tip.y * WINDOW_HEIGHT)
            # print(int(index_tip.x * 800), int(index_tip.y * 600))

        return cursor
        # cv2.imshow("Hand Tracking", frame)
        # cv2.waitKey(1)

    def cleanup(self):
        # Release the VideoCapture object
        self.cap.release()


# TODO: Create a new cursor class that tracks the index finger tip and displays it on the screen

# # Create an instance of the HandDetector class and run it
# hand_detector = HandDetector()
# while True:
#     hand_detector.get_pointer_location()
