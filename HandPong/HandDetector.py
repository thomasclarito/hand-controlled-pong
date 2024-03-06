"""@file HandDetector.py

This module contains the HandDetector class for detecting hand gestures and landmarks.
"""

import cv2
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks.python.components.containers.landmark import (
    NormalizedLandmark,
)
import numpy as np
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
        """The constructor for the HandDetector class."""

        # Create a GestureRecognizerOptions object to specify the model and the running mode
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
        """Get the location of the index finger tip.

        Args:
            cursor (Cursor): The cursor object, encapsulating the position of the cursor

        Returns:
            Cursor: The updated cursor object with the new position of the index finger tip
        """

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

            # Draw the hand landmarks on the frame
            frame = self.draw_landmarks(frame, result.hand_landmarks[0])

            # Update the cursor location to the location of the index finger
            cursor.posx = int(index_tip.x * WINDOW_WIDTH)
            cursor.posy = int(index_tip.y * WINDOW_HEIGHT)

        # Display the frame
        cv2.imshow("Hand Tracking", frame)
        cv2.waitKey(1)

        return cursor

    def check_gesture(self, gesture: str) -> bool:
        """Check if the user is making specified gesture for 20 consecutive frames.

        Args:
            gesture (str): The gesture to recognize

        Returns:
            bool: True if the gesture is recognized for 20 consecutive frames, False otherwise
        """
        for i in range(20):
            # Read the current frame from the webcam

            ret, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB, data=frame_rgb
            )
            result = self.detector.recognize(mp_image)

            if result.hand_landmarks:
                frame = self.draw_landmarks(frame, result.hand_landmarks[0])

            cv2.imshow("Hand Tracking", frame)
            cv2.waitKey(1)

            if result.gestures:
                if result.gestures[0][0].category_name == gesture:
                    continue

            return False

        return True

    def draw_landmarks(
        self, frame: np.ndarray, landmarks: NormalizedLandmark
    ) -> np.ndarray:
        """Display the hand landmarks from the results of the detector on the frame.

        Args:
            frame (np.ndarray): The frame to draw the landmarks on
            landmarks (mp.HandLandmarkList): The list of landmarks to draw
        """

        # Draw the hand landmarks of the first hand detected
        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend(
            [
                landmark_pb2.NormalizedLandmark(
                    x=landmark.x, y=landmark.y, z=landmark.z
                )
                for landmark in landmarks
            ]
        )
        mp.solutions.drawing_utils.draw_landmarks(
            frame, hand_landmarks_proto, mp.solutions.hands.HAND_CONNECTIONS
        )

        return frame

    def cleanup(self):
        # Release the VideoCapture object
        self.cap.release()
