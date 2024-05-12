import pyautogui
import cv2
import mediapipe as mp

def control_mouse():
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()

    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape

        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):  # Left eye landmarks
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))  # Draw circles for visualization
                if id == 1:  # Use the midpoint of the left eye
                    screen_x = screen_w / frame_w * x
                    screen_y = screen_h / frame_h * y
                    pyautogui.moveTo(screen_x, screen_y)

            left_eye = [landmarks[145], landmarks[159]]  # Landmarks for left eye
            right_eye = [landmarks[386], landmarks[374]]  # Landmarks for right eye

            for landmark in left_eye:  # Visualize left eye landmarks
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))

            for landmark in right_eye:  # Visualize right eye landmarks
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 0, 255))
            if (left_eye[0].y - left_eye[1].y) > 0.04:
                pyautogui.click()
                pyautogui.sleep(1)
            print(left_eye[0].y - left_eye[1].y)
            # Check for blink in the right eye
            if (right_eye[0].y - right_eye[1].y) > -0.004:
                pyautogui.rightClick()
                pyautogui.sleep(1)  # Perform a right-click action

        cv2.imshow('Eye Controlled Mouse', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
