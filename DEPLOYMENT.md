# 🚀 Deployment Guide

This guide will help you deploy your Django Voting App to various hosting platforms.

## 📋 Pre-Deployment Checklist

1. ✅ Settings updated for production
2. ✅ Static files configuration added
3. ✅ Dependencies updated (gunicorn, whitenoise)
4. ✅ Environment variables configured

## 🌐 Deployment Options

### Option 1: Railway (Recommended - Easy & Free Tier)

Railway is one of the easiest platforms to deploy Django apps.

#### Steps:

1. **Sign up at Railway**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure Environment Variables**
   - Go to your project settings
   - Add these environment variables:
     ```
     DEBUG=False
     SECRET_KEY=your-secret-key-here (generate a new one!)
     ALLOWED_HOSTS=your-app-name.railway.app
     ```
   - Generate a new SECRET_KEY:
     ```python
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```

4. **Configure Build Settings**
   - Railway will auto-detect Python
   - Make sure it uses: `python manage.py migrate && python manage.py collectstatic --noinput`

5. **Deploy**
   - Railway will automatically deploy when you push to GitHub
   - Your app will be live at: `https://your-app-name.railway.app`

6. **Create Superuser**
   - Go to Railway dashboard → Your service → Deploy logs
   - Click "Open Shell" or use Railway CLI:
     ```bash
     railway run python manage.py createsuperuser
     ```

---

### Option 2: Render (Free Tier Available)

Render offers a free tier with automatic deployments.

#### Steps:

1. **Sign up at Render**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository

3. **Configure Service**
   - **Name**: Your app name
   - **Environment**: Python 3
   - **Build Command**: 
     ```bash
     pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
     ```
   - **Start Command**: 
     ```bash
     gunicorn voting_project.wsgi
     ```

4. **Add Environment Variables**
   - Go to "Environment" tab
   - Add:
     ```
     DEBUG=False
     SECRET_KEY=your-secret-key-here
     ALLOWED_HOSTS=your-app-name.onrender.com
     ```

5. **Deploy**
   - Click "Create Web Service"
   - Render will build and deploy automatically
   - Your app: `https://your-app-name.onrender.com`

6. **Create Superuser**
   - Use Render Shell:
     ```bash
     python manage.py createsuperuser
     ```

---

### Option 3: PythonAnywhere (Beginner Friendly)

Great for learning and has a free tier.

#### Steps:

1. **Sign up at PythonAnywhere**
   - Go to https://www.pythonanywhere.com
   - Create a free account

2. **Upload Your Code**
   - Go to "Files" tab
   - Upload your project or clone from GitHub:
     ```bash
     git clone https://github.com/yourusername/django-voting-app.git
     ```

3. **Set up Virtual Environment**
   - Go to "Consoles" → "Bash"
   - Navigate to your project:
     ```bash
     cd django-voting-app
     python3.10 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

4. **Configure Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration" → Python 3.10
   - Set source code directory to your project path

5. **Configure WSGI File**
   - Click on WSGI configuration file
   - Replace content with:
     ```python
     import os
     import sys
     
     path = '/home/yourusername/django-voting-app'
     if path not in sys.path:
         sys.path.append(path)
     
     os.environ['DJANGO_SETTINGS_MODULE'] = 'voting_project.settings'
     
     from django.core.wsgi import get_wsgi_application
     application = get_wsgi_application()
     ```

6. **Set Environment Variables**
   - In WSGI file or via "Web" → "Environment variables":
     ```
     DEBUG=False
     SECRET_KEY=your-secret-key
     ```

7. **Run Migrations**
   - In Bash console:
     ```bash
     python manage.py migrate
     python manage.py collectstatic
     python manage.py createsuperuser
     ```

8. **Reload Web App**
   - Go to "Web" tab → Click "Reload"

---

## 🔐 Security Checklist

Before going live, ensure:

- [ ] `DEBUG = False` in production
- [ ] New `SECRET_KEY` generated (not the default one!)
- [ ] `ALLOWED_HOSTS` set to your domain
- [ ] SSL/HTTPS enabled (most platforms do this automatically)
- [ ] Strong admin password set
- [ ] Database backups configured (if using production database)

## 📝 Post-Deployment Steps

1. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

2. **Load Sample Data (Optional)**
   ```bash
   python manage.py create_sample_polls
   ```

3. **Test Your App**
   - Visit your live URL
   - Test voting functionality
   - Check admin dashboard

## 🐛 Troubleshooting

### Static Files Not Loading
- Run: `python manage.py collectstatic --noinput`
- Check `STATIC_ROOT` in settings.py
- Verify WhiteNoise is in `INSTALLED_APPS` middleware

### Database Errors
- Run migrations: `python manage.py migrate`
- Check database connection settings

### 500 Internal Server Error
- Check logs on your hosting platform
- Verify `DEBUG=False` and `ALLOWED_HOSTS` is set
- Check environment variables are set correctly

## 📚 Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [Railway Documentation](https://docs.railway.app)
- [Render Documentation](https://render.com/docs)
- [PythonAnywhere Help](https://help.pythonanywhere.com)

---

**Need Help?** Check the logs on your hosting platform or open an issue on GitHub!

