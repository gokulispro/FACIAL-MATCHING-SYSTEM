# # camera_capture.py
# import os
# import cv2
# import numpy as np
# import threading
# from queue import Queue
# from image_processing import FaceRecognition

# class CameraCapture:
#     def __init__(self, video_source, output_dir, cam_type='x', capture_delay=0.5):
#         self.video_source = video_source
#         self.output_dir = output_dir
#         self.cam_type = cam_type
#         self.image_queue = Queue()
#         self.live = np.zeros((360, 480, 3))
#         self.capture_delay = capture_delay
#         self.face_recognition = FaceRecognition()
#         self.running = True

#         os.makedirs(self.output_dir, exist_ok=True)

#         self.thread = threading.Thread(target=self.run)
#         self.thread.start()

#     def run(self):
#         self.cap = cv2.VideoCapture(self.video_source)
#         if not self.cap.isOpened():
#             print(f"Error capturing from video source {self.video_source}")
#             return

#         while self.running:
#             ret, frame = self.cap.read()
#             if not ret:
#                 break

#             self.live = frame
#             self.process_frame(frame)
#             cv2.waitKey(int(self.capture_delay * 1000))

#         self.cap.release()
#         self.image_queue.put("DONE")
#         print(f"Video capture from {self.video_source} finished.")

#     def process_frame(self, frame):
#         frame_count = len(os.listdir(self.output_dir)) + 1
#         frame_path = os.path.join(self.output_dir, f"frame_{frame_count}.jpg")
#         cv2.imwrite(frame_path, frame)
#         self.image_queue.put((frame_path, self.cam_type))
#         print(f"Captured {frame_path}")

#     def stop(self):
#         self.running = False
#         if hasattr(self, 'cap') and self.cap.isOpened():
#             self.cap.release()
#         cv2.destroyAllWindows()
#         print(f"Video capture from {self.video_source} stopped.")

'''''3435 nr7 787 8678989 69  7 079'''
# # camera_capture.py
# import os
# import cv2
# import numpy as np
# import threading
# from queue import Queue
# from image_processing import FaceRecognition,ImageProcessor

# class CameraCapture:
#     def __init__(self, video_source, output_dir, cam_type='x', capture_delay=0.5):
#         self.video_source = video_source
#         self.output_dir = output_dir
#         self.cam_type = cam_type
#         self.image_queue = Queue()
#         self.live = np.zeros((360, 480, 3))
#         self.capture_delay = capture_delay
#         self.face_recognition = FaceRecognition()
#         self.running = True

#         os.makedirs(self.output_dir, exist_ok=True)

#         self.thread = threading.Thread(target=self.run)
#         self.thread.start()

#     def run(self):
#         self.cap = cv2.VideoCapture(self.video_source)
#         if not self.cap.isOpened():
#             print(f"Error capturing from video source {self.video_source}")
#             return

#         while self.running:
#             ret, frame = self.cap.read()
#             if not ret:
#                 break

#             self.live = frame
#             self.process_frame(frame)
#             cv2.waitKey(int(self.capture_delay * 1000))

#         self.cap.release()
#         self.image_queue.put("DONE")
#         print(f"Video capture from {self.video_source} finished.")

#     def process_frame(self, frame):
#         analyses = self.face_recognition.evaluate_image(frame)
#         if analyses:
#             frame_count = len(os.listdir(self.output_dir)) + 1
#             frame_path = os.path.join(self.output_dir, f"frame_{frame_count}.jpg")
#             cv2.imwrite(frame_path, frame)
#             self.image_queue.put((frame_path, self.cam_type))
#             print(f"Captured {frame_path} because a person was detected")

#     def stop(self):
#         self.running = False
#         if hasattr(self, 'cap') and self.cap.isOpened():
#             self.cap.release()
#         cv2.destroyAllWindows()
#         print(f"Video capture from {self.video_source} stopped.")

# camera_capture.py
import os
import cv2
import numpy as np
import threading
from queue import Queue
from image_processing import FaceRecognition

class CameraCapture:
    def __init__(self, video_source, output_dir, cam_type='x', capture_delay=0.5):
        self.video_source = video_source
        self.output_dir = output_dir
        self.cam_type = cam_type
        self.image_queue = Queue()
        self.live = np.zeros((360, 480, 3))
        self.capture_delay = capture_delay
        self.face_recognition = FaceRecognition()
        self.running = True

        os.makedirs(self.output_dir, exist_ok=True)

        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        self.cap = cv2.VideoCapture(self.video_source)
        if not self.cap.isOpened():
            print(f"Error capturing from video source {self.video_source}")
            return

        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Reduce the resolution for display
            display_frame = cv2.resize(frame, (640, 480))  # Resize for display purposes
            self.live = display_frame

            # Process the frame for person detection
            self.process_frame(frame)
            cv2.waitKey(1)  # A small delay to allow the frame to be displayed

        self.cap.release()
        self.image_queue.put("DONE")
        print(f"Video capture from {self.video_source} finished.")

    def process_frame(self, frame):
        analyses = self.face_recognition.evaluate_image(frame)
        if analyses:
            frame_count = len(os.listdir(self.output_dir)) + 1
            frame_path = os.path.join(self.output_dir, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)
            self.image_queue.put((frame_path, self.cam_type))
            print(f"Captured {frame_path} because a person was detected")

    def stop(self):
        self.running = False
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()
        print(f"Video capture from {self.video_source} stopped.")


