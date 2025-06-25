# 🍳 Recipe Manager

A **Django 5** mini-app for storing, tagging, and searching recipes.  
Spin it up locally in minutes or explore the live demo below.

---

## 🌐 Live Demo

> **https://recipe-app-3-4090.onrender.com/**

*(Free Render tier – may sleep after inactivity; first load can take ~30 s.)*

---

## 🖥️ Requirements

| Tool | Version |
|------|---------|
| Python | **3.10 or newer** |
| Git | 2.x |
| Terminal | PowerShell (Windows) or Bash (macOS / Linux) |

Everything else is installed inside a **virtual environment**.

---

## 🚀 Quick Start

```bash
# 1  Clone the repo
git clone https://github.com/DragonOfUnkown/RECIPE_APP.git
cd RECIPE_APP          # project root

# 2  Create & activate a virtualenv
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3  Install dependencies
pip install -r requirements.txt

# 4  Bootstrap the SQLite database
python manage.py migrate

# 5  (optional) create an admin user
python manage.py createsuperuser

# 6  Run the development server
python manage.py runserver
Now open http://127.0.0.1:8000 in your browser.
The Django admin lives at http://127.0.0.1:8000/admin.

here is the live app : https://recipe-app-3-4090.onrender.com/