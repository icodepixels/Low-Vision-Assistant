from flask import Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from app.camera import Camera
from app.object_detection import ObjectDetector
from gtts import gTTS

main = Blueprint('main', __name__)
camera = Camera()
detector = ObjectDetector()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/capture', methods=['POST'])
def capture():
    try:
        # Generate unique filename
        filename = secure_filename(f"capture_{os.urandom(8).hex()}.jpg")
        save_path = os.path.join(main.root_path, 'static', 'uploads', filename)

        # Capture image
        camera.capture_image(save_path)

        # Detect objects
        detections = detector.detect_objects(save_path)

        # Generate audio description
        description = "I can see: " + ", ".join([d['label'] for d in detections])
        audio_file = f"description_{os.urandom(8).hex()}.mp3"
        audio_path = os.path.join(main.root_path, 'static', 'uploads', audio_file)
        tts = gTTS(text=description, lang='en')
        tts.save(audio_path)

        return jsonify({
            'success': True,
            'image': f'/static/uploads/{filename}',
            'audio': f'/static/uploads/{audio_file}',
            'detections': detections
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@main.route('/release', methods=['POST'])
def release_camera():
    camera.release()
    return jsonify({'success': True})