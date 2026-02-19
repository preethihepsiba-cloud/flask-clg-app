from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from database import get_db_connection
from config import Config
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config.from_object(Config)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        phone = request.form['phone'].strip()
        course = request.form['course'].strip()

        file = request.files['photo']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join('static/uploads', f"{int(os.times()[4])}_{filename}")
            file.save(filepath)

            conn = get_db_connection()
            cur = conn.cursor()
            try:
                cur.execute(
                    "INSERT INTO students (name, email, phone, course, photo) VALUES (?, ?, ?, ?, ?)",
                    (name, email, phone, course, filepath)
                )
                conn.commit()
                flash("Student Registered Successfully!", "success")
            except Exception as e:
                flash(f"Error: {e}", "danger")
            finally:
                conn.close()
        else:
            flash("Invalid file type. Only PNG, JPG, JPEG allowed.", "danger")

        return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/view')
def view():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()
    return render_template('view.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
