# SocialApp 🌐

A full-stack social media web application built with Django and Tailwind CSS.

## 🚀 Features

- User registration and authentication
- Create, edit and delete posts
- Like and comment on posts
- Follow and unfollow users
- Personalized feed
- User profiles with profile pictures
- Search users and posts
- Notifications for likes, comments and follows
- Responsive design with DaisyUI

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Tailwind CSS + DaisyUI
- **Database:** SQLite (development)
- **Storage:** Pillow for image handling

## ⚙️ How to Run Locally

1. Clone the repository
```bash
git clone https://github.com/Barshajit-Chakraborti/SocialApp
cd socialapp
```

2. Create and activate virtual environment
```bash
python -m venv .venv --upgrade-deps
.venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
# Terminal 1
python manage.py tailwind start

# Terminal 2
python manage.py runserver
```



## 📸 Screenshots
(Add screenshots of your app here)

## 👤 Author
Barshajit : chakrabortibarshajit@gmail.com