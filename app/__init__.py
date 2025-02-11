from flask import Flask
from pathlib import Path

def create_app():
    app = Flask(__name__)

    # Ensure upload directory exists
    upload_dir = Path(app.root_path) / 'static' / 'uploads'
    upload_dir.mkdir(parents=True, exist_ok=True)

    # Configure upload folder
    app.config['UPLOAD_FOLDER'] = str(upload_dir)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

    # Register routes
    from app import routes
    app.register_blueprint(routes.main)

    return app