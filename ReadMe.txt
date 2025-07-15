Driver Drowsiness Detection Project
------------------------------------

1. Open your project in VS Code.
2. Open Terminal (Terminal -> New Terminal).
3. Create venv: python -m venv venv...
   py -3.13 -m venv venv
4. Activate venv:
    Windows: venv\Scripts\activate
    Linux/Mac: source venv/bin/activate
5. Install requirements: pip install opencv-python dlib scipy pandas matplotlib
6. Run GUI: python app_gui.py
    py -3.13 app_gui.py
7. Use buttons to demonstrate detection, logs, graphs.

Ensure 'utils/shape_predictor_68_face_landmarks.dat' is downloaded from:
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2


 py -3.10 -m venv venv310
 .\venv310\Scripts\Activate
 python app_gui.py
 