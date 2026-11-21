# SocialApp 🌐

A full-stack social media web application built with **Django** and **Tailwind CSS**. Share posts, follow people, and stay up to date with a personalized feed and real-time-style notifications.

## 🚀 Features

**Accounts & Profiles**
- User registration, login and logout
- Profile pages with profile pictures

**Posts & Engagement**
- Create, edit and delete posts
- Like and comment on posts

**Social Graph**
- Follow and unfollow other users
- Personalized feed based on who you follow

**Discovery & Alerts**
- Search for users and posts
- Notifications for likes, comments and new followers

**UI**
- Fully responsive layout built with Tailwind CSS and DaisyUI

---

## 🛠️ Tech Stack

| Layer     | Technology                                |
|-----------|-------------------------------------------|
| Backend   | Django (Python)                           |
| Frontend  | Django templates, Tailwind CSS, DaisyUI   |
| Database  | SQLite (development)                      |
| Media     | Pillow for image handling                 |
| Tooling   | Node.js / npm (for the Tailwind build)    |

---

---

## 📂 Project Structure

```
SocialApp/
├── core/            # Main app: models, views, templates for posts, profiles, follows
├── socialapp/       # Django project settings, URLs, WSGI/ASGI config
├── theme/           # Tailwind CSS app (django-tailwind)
├── manage.py        # Django management entry point
├── package.json     # Node dependencies for Tailwind
└── README.md
```

---

## ⚡ Getting Started

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [Node.js and npm](https://nodejs.org/) (required to compile Tailwind CSS)
- [Git](https://git-scm.com/)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Barshajit-Chakraborti/SocialApp.git
cd SocialApp
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv --upgrade-deps
```

- Windows: `.venv\Scripts\activate`
- macOS / Linux: `source .venv/bin/activate`

**3. Install Python dependencies**

```bash
pip install -r requirements.txt
```

**4. Install Tailwind dependencies**

```bash
python manage.py tailwind install
```

**5. Apply database migrations**

```bash
python manage.py migrate
```

**6. Create an admin account**

```bash
python manage.py createsuperuser
```

**7. Start the development servers**

Tailwind and Django each need their own terminal:

```bash
# Terminal 1 – compile and watch Tailwind CSS
python manage.py tailwind start

# Terminal 2 – run the Django server
python manage.py runserver
```

---

## 💡 Usage

1. **Sign up** for an account and set up your profile picture.
2. **Follow** other users to populate your feed.
3. **Post**, **like** and **comment** to interact with the community.
4. Use **search** to find people and posts.
5. Check **notifications** to see who has liked, commented or followed you.

The Django admin panel is available at `/admin/` using your superuser credentials.

---

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

---

## 👤 Author

**Barshajit Chakraborti**

- GitHub: [@Barshajit-Chakraborti](https://github.com/Barshajit-Chakraborti)
- Email: [chakrabortibarshajit@gmail.com](mailto:chakrabortibarshajit@gmail.com)

---
