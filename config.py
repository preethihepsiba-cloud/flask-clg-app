import os

class Config:
    SECRET_KEY = 'admin@123'
    DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'studentdb.sqlite3')
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB
