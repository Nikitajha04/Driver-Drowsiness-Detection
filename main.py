
# import cv2
# from utils.drowsiness_detection import detect_drowsiness

# def main():
#     detect_drowsiness()

# if __name__ == "__main__":
#     main()

import cv2
import os
from utils.drowsiness_detection import detect_drowsiness

def main():
    try:
        # Construct absolute path to the model
        script_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(script_dir, "models", "shape_predictor_68_face_landmarks.dat")
        
        # Check if the model exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Model file not found:\n{model_path}\n"
                "Make sure 'shape_predictor_68_face_landmarks.dat' is in the 'models/' directory."
            )

        print("[INFO] Starting Driver Drowsiness Detection...")
        print("[INFO] Initializing Driver Drowsiness Detection...")
        print("[INFO] Press 'ESC' to quit detection.")

        # Call the detection function with model path
        detect_drowsiness(model_path)

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()

