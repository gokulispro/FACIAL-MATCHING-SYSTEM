# image_processing.py
import os
import cv2
import numpy as np
import face_recognition
import dlib

class FaceRecognition:
    def __init__(self, model_path='shape_predictor_68_face_landmarks.dat'):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(model_path)

    def eye_aspect_ratio(self, eye):
        A = np.linalg.norm(np.array(eye[1]) - np.array(eye[5]))
        B = np.linalg.norm(np.array(eye[2]) - np.array(eye[4]))
        C = np.linalg.norm(np.array(eye[0]) - np.array(eye[3]))
        return (A + B) / (2.0 * C)

    def mouth_aspect_ratio(self, mouth):
        A = np.linalg.norm(np.array(mouth[3]) - np.array(mouth[9]))
        B = np.linalg.norm(np.array(mouth[2]) - np.array(mouth[10]))
        C = np.linalg.norm(np.array(mouth[4]) - np.array(mouth[8]))
        D = np.linalg.norm(np.array(mouth[0]) - np.array(mouth[6]))
        return (A + B + C) / (3.0 * D)

    def analyze_facial_landmarks(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray)
        results = []

        for face in faces:
            landmarks = self.predictor(gray, face)
            left_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
            right_eye = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]
            mouth = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(48, 68)]
            results.append((left_eye, right_eye, mouth, face))
        return results

    def evaluate_image(self, image):
        landmarks_list = self.analyze_facial_landmarks(image)
        if not landmarks_list:
            return []

        evaluations = []
        for landmarks in landmarks_list:
            left_eye, right_eye, mouth, face = landmarks
            left_ear = self.eye_aspect_ratio(left_eye)
            right_ear = self.eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2.0
            mar = self.mouth_aspect_ratio(mouth)

            smiling = mar > 0.5
            eyes_open = ear > 0.2
            clarity = cv2.Laplacian(image, cv2.CV_64F).var()

            evaluations.append({
                "smiling": smiling,
                "eyes_open": eyes_open,
                "clarity": clarity,
                "face": face
            })
        return evaluations

class ImageProcessor:
    def __init__(self, grouped_dir, best_dir, y_dir, matched_dir, known_encodings=None, tolerance=0.57):
        self.grouped_dir = grouped_dir
        self.best_dir = best_dir
        self.y_dir = y_dir
        self.matched_dir = matched_dir
        self.face_recognition = FaceRecognition()
        self.known_encodings = known_encodings if known_encodings else []
        self.tolerance = tolerance
        os.makedirs(self.grouped_dir, exist_ok=True)
        os.makedirs(self.best_dir, exist_ok=True)
        os.makedirs(self.y_dir, exist_ok=True)
        os.makedirs(self.matched_dir, exist_ok=True)

    def process_image(self, image_path, cam_type='x'):
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) == 0:
            return

        if cam_type == 'x':
            for encoding in encodings:
                matches = face_recognition.compare_faces(self.known_encodings, encoding, tolerance=self.tolerance)
                if True in matches:
                    match_index = matches.index(True)
                else:
                    self.known_encodings.append(encoding)
                    match_index = len(self.known_encodings) - 1

                person_dir = os.path.join(self.grouped_dir, f"person_{match_index + 1}")
                os.makedirs(person_dir, exist_ok=True)

                image_name = os.path.basename(image_path)
                cv2.imwrite(os.path.join(person_dir, image_name), cv2.imread(image_path))
                print(f"Grouped {image_name} under person_{match_index + 1}")
        else:  # Camera Y
            image_name = os.path.basename(image_path)
            cv2.imwrite(os.path.join(self.y_dir, image_name), cv2.imread(image_path))
            print(f"Saved {image_name} from Camera Y")

    def get_top_images(self, top_n=1):
        for person_dir in os.listdir(self.grouped_dir):
            full_person_dir = os.path.join(self.grouped_dir, person_dir)
            if not os.path.isdir(full_person_dir):
                continue

            images_with_scores = []

            for img_name in os.listdir(full_person_dir):
                img_path = os.path.join(full_person_dir, img_name)
                if not os.path.isfile(img_path):
                    continue

                image = cv2.imread(img_path)
                analyses = self.face_recognition.evaluate_image(image)
                for analysis in analyses:
                    if analysis:
                        score = analysis["clarity"]
                        if analysis["smiling"]:
                            score += 10
                        if analysis["eyes_open"]:
                            score += 5

                        images_with_scores.append((img_path, score))

            images_with_scores.sort(key=lambda x: x[1], reverse=True)
            top_images = images_with_scores[:top_n]

            for idx, (img_path, score) in enumerate(top_images):
                top_image_name = f'{person_dir}_best_{idx + 1}.jpg'
                cv2.imwrite(os.path.join(self.best_dir, top_image_name), cv2.imread(img_path))
                print(f"Top {idx + 1} image for {person_dir} saved as {top_image_name}")

    def compare_and_store_best_images(self):
        encodings_x = []
        images_x = []

        for img_name in os.listdir(self.best_dir):
            img_path = os.path.join(self.best_dir, img_name)
            if not os.path.isfile(img_path):
                continue

            image = face_recognition.load_image_file(img_path)
            encodings = face_recognition.face_encodings(image)
            if len(encodings) > 0:
                encodings_x.extend(encodings)
                images_x.append(img_path)

        for img_name in os.listdir(self.y_dir):
            img_path = os.path.join(self.y_dir, img_name)
            if not os.path.isfile(img_path):
                continue

            image = face_recognition.load_image_file(img_path)
            encodings = face_recognition.face_encodings(image)
            if len(encodings) == 0:
                continue

            for encoding in encodings:
                matches = face_recognition.compare_faces(encodings_x, encoding, tolerance=self.tolerance)
                if True in matches:
                    match_index = matches.index(True)
                    matched_image = images_x[match_index]
                    matched_image_name = os.path.basename(matched_image)
                    matched_output_path = os.path.join(self.matched_dir, f"match_{matched_image_name}")

                    os.makedirs(self.matched_dir, exist_ok=True)
                    cv2.imwrite(matched_output_path, cv2.imread(matched_image))
                    print(f"Match found! {matched_image_name} saved as {matched_output_path}")
                    return matched_output_path  # Return matched path for real-time display


