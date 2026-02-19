# 🎓 Flask Student Registration System

A simple **student registration system** with photo upload built using:

- Python Flask
- SQLite (no separate DB server required)
- Bootstrap 5
- Gunicorn for production
- VM Deployment on Debian/Ubuntu

---

## 📁 Project Structure

flask-clg-app/
├── app.py
├── database.py
├── config.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── register.html
│ └── view.html
├── static/
│ └── uploads/
│ └── .gitkeep
├── requirements.txt
└── README.md


---

## 📌 Features

- Student Registration Form with Photo Upload  
- View Registered Students  
- SQLite Database (file-based, portable)  
- Bootstrap 5 UI Styling  
- Flash Messages for Success/Error  

---

## 🚀 Deployment Guide (Debian / Ubuntu VM)

### 1️⃣ Update and Install Dependencies

```bash
sudo apt update
sudo apt install python3-venv python3-full -y
sudo apt install git -y

2️⃣ Clone the Repository
git clone https://github.com/preethihepsiba-cloud/flask-clg-app.git
cd flask-clg-app

3️⃣ Set up Python Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

4️⃣ SQLite Database Setup
The app automatically creates the SQLite database and students table on the first run.  If you want to initialize manually:

python3
>>> from database import init_db
>>> init_db()
>>> exit()
This will create a studentdb.sqlite3 file in the project folder.

5️⃣ Configure Firewall (Google Cloud / VM)
Go to VPC-->Firewall-->Add Firewall Rule
Name: gunicorn-rule
Direction: Ingress
Target: All instances
Source IP Range: 0.0.0.0/0
Protocol: TCP
Port: 5000

VM --> Networking --> Network Tags
Tag your VM with gunicorn-rule to apply the rule.

6️⃣ Run the App with Gunicorn
source venv/bin/activate
gunicorn -b 0.0.0.0:5000 app:app
The app will be available on your external IP:

http://[EXTERNAL-IP]/

7️⃣ Access URLs
Home / Index: /
Register Student: /register
View Students: /view