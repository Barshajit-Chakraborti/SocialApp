# SocialApp 🌐

A full-stack social media web application built with Django and Tailwind CSS.A full-stack social media web application built with Django and Tailwind CSS. Share posts, follow people, and stay up to date with a personalized feed and real-time-style notifications.

🚀 Features

Accounts & Profiles

User registration, login and logout
Profile pages with profile pictures

Posts & Engagement

Create, edit and delete posts
Like and comment on posts

Social Graph

Follow and unfollow other users
Personalized feed based on who you follow

Discovery & Alerts

Search for users and posts
Notifications for likes, comments and new followers

UI

Fully responsive layout built with Tailwind CSS and DaisyUI
🛠️ Tech Stack
Layer	Technology
Backend	Django (Python)
Frontend	Django templates, Tailwind CSS, DaisyUI
Database	SQLite (development)
Media	Pillow for image handling
Tooling	Node.js / npm (for the Tailwind build)
📸 Screenshots

Add screenshots to a docs/screenshots/ folder and reference them here.

Home Feed	Profile	Notifications
Feed	Profile	Notifications
📂 Project Structure
SocialApp/
├── core/            # Main app: models, views, templates for posts, profiles, follows
├── socialapp/       # Django project settings, URLs, WSGI/ASGI config
├── theme/           # Tailwind CSS app (django-tailwind)
├── manage.py        # Django management entry point
├── package.json     # Node dependencies for Tailwind
└── README.md
⚡ Getting Started
Prerequisites
Python 3.10+
Node.js and npm (required to compile Tailwind CSS)
Git
Installation

1. Clone the repository

bash
git clone https://github.com/Barshajit-Chakraborti/SocialApp.git
cd SocialApp

2. Create and activate a virtual environment

bash
python -m venv .venv --upgrade-deps
Windows: .venv\Scripts\activate
macOS / Linux: source .venv/bin/activate

3. Install Python dependencies

bash
pip install -r requirements.txt

4. Install Tailwind dependencies

bash
python manage.py tailwind install

5. Apply database migrations

bash
python manage.py migrate

6. Create an admin account

bash
python manage.py createsuperuser

7. Start the development servers

Tailwind and Django each need their own terminal:

bash
# Terminal 1 – compile and watch Tailwind CSS
python manage.py tailwind start

# Terminal 2 – run the Django server
python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

🔧 Configuration

For anything beyond local development, don't use the default settings. Before deploying:

Move SECRET_KEY out of settings.py and into an environment variable
Set DEBUG = False
Configure ALLOWED_HOSTS
Switch from SQLite to a production database such as PostgreSQL
Configure MEDIA_ROOT / MEDIA_URL and serve uploaded files properly
Run python manage.py tailwind build to produce the production CSS
💡 Usage
Sign up for an account and set up your profile picture.
Follow other users to populate your feed.
Post, like and comment to interact with the community.
Use search to find people and posts.
Check notifications to see who has liked, commented or followed you.

The Django admin panel is available at /admin/ using your superuser credentials.

🗺️ Roadmap
[ ] Direct messaging
[ ] Hashtags and trending topics
[ ] Image/video attachments in posts
[ ] Real-time notifications (WebSockets)
[ ] REST API
[ ] Docker setup
[ ] Automated tests and CI
🤝 Contributing

Contributions, issues and feature requests are welcome!

Fork the repository
Create a feature branch: git checkout -b feature/your-feature
Commit your changes: git commit -m "Add your feature"
Push to the branch: git push origin feature/your-feature
Open a Pull Request
📄 License

No license has been specified yet. Add a LICENSE file (for example MIT) to let others know how they can use this project.

👤 Author

Barshajit Chakraborti

GitHub: @Barshajit-Chakraborti
Email: chakrabortibarshajit@gmail.com
