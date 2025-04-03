# # main.py
# import cv2
# import time
# from camera_capture import CameraCapture
# from image_processing import ImageProcessor
# import threading

# def process_images(camera_capture, processor):
#     while True:
#         item = camera_capture.image_queue.get()
#         if item == "DONE":
#             break

#         image_path, cam_type = item
#         processor.process_image(image_path, cam_type)
#         if cam_type == 'x':
#             processor.get_top_images()

# def display_matched_images(processor):
#     while True:
#         matched_image_path = processor.compare_and_store_best_images()
#         if matched_image_path:
#             matched_image = cv2.imread(matched_image_path)
#             if matched_image is not None:
#                 cv2.imshow("Matched Image", matched_image)
#                 cv2.waitKey(500)  # Display each matched image for 0.5 seconds
#         time.sleep(1)

# def main():
#     url1 = 'http://172.16.66.95:5000/video_feed'
#     url2 = 'http://172.16.66.166:5000/video_feed'  # Replace with another URL if different

#     camera1 = CameraCapture(url1, 'ik/x', cam_type='x')
#     camera2 = CameraCapture(url2, 'ik/y', cam_type='y')

#     time.sleep(1)  # Allow some time for initial captures

#     processor = ImageProcessor('ik/x_grouped', 'ik/x_best', 'ik/y', 'ik/matched')

#     camera1_thread = threading.Thread(target=process_images, args=(camera1, processor))
#     camera2_thread = threading.Thread(target=process_images, args=(camera2, processor))

#     camera1_thread.start()
#     camera2_thread.start()

#     display_thread = threading.Thread(target=display_matched_images, args=(processor,))
#     display_thread.start()

#     while camera1_thread.is_alive() or camera2_thread.is_alive():
#         frame1 = camera1.live
#         frame2 = camera2.live

#         if frame1.any() and frame2.any():
#             cv2.imshow("Camera 1", frame1)
#             cv2.imshow("Camera 2", frame2)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             camera1.stop()
#             camera2.stop()
#             break

#         time.sleep(0.1)

#     cv2.destroyAllWindows()

#     camera1_thread.join()
#     camera2_thread.join()
#     display_thread.join()

#     print("Completed all processing tasks.")

# if __name__ == '__main__':
#     main()

'''eretiretwuiuwitriwurtw;iweri tu'''





# # main.py
# import cv2
# import time
# from camera_capture import CameraCapture
# from image_processing import ImageProcessor
# import threading

# def process_images(camera_capture, processor):
#     while True:
#         item = camera_capture.image_queue.get()
#         if item == "DONE":
#             break

#         image_path, cam_type = item
#         processor.process_image(image_path, cam_type)
#         if cam_type == 'x':
#             processor.get_top_images()

# def display_matched_images(processor):
#     while True:
#         matched_image_path = processor.compare_and_store_best_images()
#         if matched_image_path:
#             matched_image = cv2.imread(matched_image_path)
#             if matched_image is not None:
#                 cv2.imshow("Matched Image", matched_image)
#                 cv2.waitKey(500)  # Display each matched image for 0.5 seconds
#         time.sleep(1)

# def main():
#     url1 = 'http://172.16.66.95:5000/video_feed'
#     url2 = 'http://172.16.66.166:5000/video_feed'  # Replace with another URL if different

#     camera1 = CameraCapture(url1, 'ik/x', cam_type='x')
#     camera2 = CameraCapture(url2, 'ik/y', cam_type='y')

#     time.sleep(1)  # Allow some time for initial captures

#     processor = ImageProcessor('ik/x_grouped', 'ik/x_best', 'ik/y', 'ik/matched')

#     camera1_thread = threading.Thread(target=process_images, args=(camera1, processor))
#     camera2_thread = threading.Thread(target=process_images, args=(camera2, processor))

#     camera1_thread.start()
#     camera2_thread.start()

#     display_thread = threading.Thread(target=display_matched_images, args=(processor,))
#     display_thread.start()

#     while camera1_thread.is_alive() or camera2_thread.is_alive():
#         frame1 = camera1.live
#         frame2 = camera2.live

#         if frame1.any() and frame2.any():
#             cv2.imshow("Camera 1", frame1)
#             cv2.imshow("Camera 2", frame2)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             camera1.stop()
#             camera2.stop()
#             break

#         time.sleep(0.1)

#     cv2.destroyAllWindows()

#     camera1_thread.join()
#     camera2_thread.join()
#     display_thread.join()

#     print("Completed all processing tasks.")

# if __name__ == '__main__':
#     main()
'''434534dre t9er'''

# # main.py
# import cv2
# import time
# from camera_capture import CameraCapture
# from image_processing import ImageProcessor
# import threading

# def process_images(camera_capture, processor):
#     while True:
#         item = camera_capture.image_queue.get()
#         if item == "DONE":
#             break

#         image_path, cam_type = item
#         processor.process_image(image_path, cam_type)
#         if cam_type == 'x':
#             processor.get_top_images()

# def display_matched_images(processor):
#     while True:
#         matched_image_path = processor.compare_and_store_best_images()
#         if matched_image_path:
#             matched_image = cv2.imread(matched_image_path)
#             if matched_image is not None:
#                 cv2.imshow("Matched Image", matched_image)
#                 cv2.waitKey(500)  # Display each matched image for 0.5 seconds
#         time.sleep(1)

# def main():
#     url1 = 'http://172.16.66.95:5000/video_feed'
#     url2 = 'http://172.16.66.166:5000/video_feed'  # Replace with another URL if different

#     camera1 = CameraCapture(url1, 'ik/x', cam_type='x')
#     camera2 = CameraCapture(url2, 'ik/y', cam_type='y')

#     time.sleep(1)  # Allow some time for initial captures

#     processor = ImageProcessor('ik/x_grouped', 'ik/x_best', 'ik/y', 'ik/matched')

#     camera1_thread = threading.Thread(target=process_images, args=(camera1, processor))
#     camera2_thread = threading.Thread(target=process_images, args=(camera2, processor))

#     camera1_thread.start()
#     camera2_thread.start()

#     display_thread = threading.Thread(target=display_matched_images, args=(processor,))
#     display_thread.start()

#     while camera1_thread.is_alive() or camera2_thread.is_alive():
#         frame1 = camera1.live
#         frame2 = camera2.live

#         if frame1.any():
#             cv2.imshow("Camera 1", frame1)
#         if frame2.any():
#             cv2.imshow("Camera 2", frame2)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             camera1.stop()
#             camera2.stop()
#             break

#         time.sleep(0.1)

#     cv2.destroyAllWindows()

#     camera1_thread.join()
#     camera2_thread.join()
#     display_thread.join()

#     print("Completed all processing tasks.")

# if __name__ == '__main__':
#     main()

'''''MAIN'''

# main.py
import cv2
import time
from camera_capture import CameraCapture
from image_processing import ImageProcessor
import threading
import os



# Process images captured from the camera
def process_images(camera_capture, processor):
    while True:
        item = camera_capture.image_queue.get()
        if item == "DONE":
            break

        image_path, cam_type = item
        processor.process_image(image_path, cam_type)
        if cam_type == 'x':
            processor.get_top_images()

# Function to display matched images
def display_matched_images(processor):

    previous_window_name = None
    while True:
        matched_image_path = processor.compare_and_store_best_images()
        if matched_image_path:
            matched_image = cv2.imread(matched_image_path)
            if matched_image is not None:
                # Close the previous window if it exists
                if previous_window_name:
                    cv2.destroyWindow(previous_window_name)

                # Generate a new window name
                window_name = f"Matched Image {os.path.basename(matched_image_path)}"
                cv2.imshow(window_name, matched_image)
                previous_window_name = window_name
                cv2.waitKey(500)  # Display each matched image for 0.5 seconds

        time.sleep(1)

def main():
    url1 = 'http://172.16.66.95:5000/video_feed'
    url2 = 'http://172.16.66.166:5000/video_feed'  # Replace with another URL if different

    camera1 = CameraCapture(url2, 'ik/x', cam_type='x')
    camera2 = CameraCapture(url1, 'ik/y', cam_type='y')

    time.sleep(1)  # Allow some time for initial captures

    processor = ImageProcessor('ik/x_grouped', 'ik/x_best', 'ik/y', 'ik/matched')

    camera1_thread = threading.Thread(target=process_images, args=(camera1, processor))
    camera2_thread = threading.Thread(target=process_images, args=(camera2, processor))

    camera1_thread.start()
    camera2_thread.start()

    display_thread = threading.Thread(target=display_matched_images, args=(processor,))
    display_thread.start()

    while camera1_thread.is_alive() or camera2_thread.is_alive():
        frame1 = camera1.live
        frame2 = camera2.live

        if frame1.any():
            cv2.imshow("Camera 1", frame1)
        if frame2.any():
            cv2.imshow("Camera 2", frame2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera1.stop()
            camera2.stop()
            break

        time.sleep(0.1)

    cv2.destroyAllWindows()

    camera1_thread.join()
    camera2_thread.join()
    display_thread.join()

    print("Completed all processing tasks.")

if __name__ == '__main__':
    main()
