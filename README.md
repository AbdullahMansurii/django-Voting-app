# 🗳️ Django Voting App

A modern, feature-rich online polling and voting web application built with Django. Create polls, collect votes, and view real-time results with a beautiful, responsive UI.

![Django](https://img.shields.io/badge/Django-5.2.8-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### Public Interface
- **Modern UI/UX Design** - Beautiful, minimalistic interface with Tailwind CSS
- **Active Polls Display** - Featured active poll with animated shine effect
- **Multi-Option Voting** - Support for polls with multiple choice options
- **Filter Toggle** - Switch between Active and Past polls
- **Real-Time Results** - View poll results with visual progress bars and percentages
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices

### Admin Dashboard
- **Dark Theme Dashboard** - Modern dark theme with semi-transparent cards
- **Statistics Overview** - Quick stats on total polls, active polls, votes, and more
- **Quick Actions** - Fast access to create polls, manage content, and view public site
- **Recent Polls** - View and edit recently created polls
- **Top Polls** - See polls with the most votes
- **Enhanced Admin Interface** - Custom admin site with improved UX

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-voting-app.git
   cd django-voting-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv_VotingApp
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv_VotingApp\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv_VotingApp/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data (optional)**
   ```bash
   python manage.py create_sample_polls
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Public site: http://127.0.0.1:8000/
   - Admin dashboard: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
PY_VotingApp/
├── polls/                    # Main polls application
│   ├── models.py            # Poll and Choice models
│   ├── views.py             # View functions
│   ├── admin.py             # Custom admin configuration
│   ├── urls.py              # URL routing
│   ├── templates/           # HTML templates
│   └── management/           # Custom management commands
├── voting_project/          # Django project settings
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── templates/               # Custom admin templates
│   └── admin/               # Admin dashboard templates
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## 🎯 Usage

### Creating a Poll

1. Log in to the admin dashboard at `/admin/`
2. Click "Create New Poll" or navigate to Polls → Add Poll
3. Fill in the poll title and question
4. Add multiple choice options
5. Set the poll status (Active/Inactive) and end date
6. Save the poll

### Voting

1. Visit the public site at `/`
2. Browse active polls
3. Click "Vote" on any poll
4. Select one or more options (multi-select supported)
5. Submit your vote
6. View results immediately

### Viewing Results

- Click "Results" on any poll card to see detailed statistics
- Results show vote counts, percentages, and visual progress bars
- View results for both active and past polls

## 🛠️ Custom Management Commands

### Create Sample Polls
```bash
python manage.py create_sample_polls
```
This command creates sample polls with choices for testing purposes.

## 🎨 Technology Stack

- **Backend**: Django 5.2.8
- **Frontend**: Tailwind CSS (via CDN)
- **Database**: SQLite (default, easily switchable to PostgreSQL/MySQL)
- **Python**: 3.8+

## 📝 Key Features Explained

### Models
- **Poll**: Represents a poll with title, question, status, and end date
- **Choice**: Represents voting options within a poll with vote counts

### Views
- **index**: Main page displaying all polls with filtering
- **vote**: Voting interface for submitting votes
- **results**: Results page showing vote statistics

### Admin Features
- Custom admin site with dark theme
- Dashboard with statistics and quick actions
- Enhanced list and form views
- Quick action buttons for efficient management

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created with ❤️ using Django

## 🙏 Acknowledgments

- Django framework for the robust backend
- Tailwind CSS for the beautiful UI components
- All contributors and users of this project

---

**Note**: This is a development project. For production use, make sure to:
- Set `DEBUG = False` in settings.py
- Configure proper database (PostgreSQL recommended)
- Set up proper static file serving
- Use environment variables for sensitive data
- Configure proper security settings

