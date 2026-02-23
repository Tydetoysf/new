# Sosa Services - Deployment Guide

## Local Development Setup

### 1. Install Dependencies

```bash
pip install flask flask-sqlalchemy flask-socketio python-telebot flask-migrate
```

### 2. Configure Environment

Edit `web/backend/config.py`:
- Update `TELEGRAM_BOT` token (get from @BotFather on Telegram)
- Update `TELEGRAM_CHAT_ID` for notifications
- Change `app.secret_key` to a secure random value

### 3. Initialize Database

```bash
cd web/backend
python database.py
```

### 4. Run Locally

```bash
python app.py
```

Access at: `http://localhost:8888`

---

## Production Deployment Options

### Option 1: Traditional VPS (DigitalOcean, Linode, Vultr)

#### Requirements:
- Ubuntu 20.04+ or similar Linux distribution
- 1GB+ RAM
- Python 3.8+
- Domain name (optional but recommended)

#### Steps:

1. **Update system and install dependencies:**
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv nginx -y
```

2. **Clone/upload your project:**
```bash
cd /var/www
sudo mkdir sosa-services
sudo chown $USER:$USER sosa-services
cd sosa-services
# Upload your files here
```

3. **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask flask-sqlalchemy flask-socketio python-telebot flask-migrate gunicorn
```

4. **Initialize database:**
```bash
cd web/backend
python database.py
cd ../..
```

5. **Create systemd service:**
```bash
sudo nano /etc/systemd/system/sosa-services.service
```

Add:
```ini
[Unit]
Description=Sosa Services Flask App
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/sosa-services/web/backend
Environment="PATH=/var/www/sosa-services/venv/bin"
ExecStart=/var/www/sosa-services/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8888 app:app

[Install]
WantedBy=multi-user.target
```

6. **Configure Nginx:**
```bash
sudo nano /etc/nginx/sites-available/sosa-services
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8888;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /socket.io {
        proxy_pass http://127.0.0.1:8888/socket.io;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

7. **Enable and start services:**
```bash
sudo ln -s /etc/nginx/sites-available/sosa-services /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl enable sosa-services
sudo systemctl start sosa-services
```

8. **Setup SSL (recommended):**
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

---

### Option 2: PythonAnywhere (Easy, Free Tier Available)

1. Sign up at https://www.pythonanywhere.com
2. Upload your files via Files tab
3. Create a new web app (Flask)
4. Configure WSGI file to point to your app
5. Set working directory to `/home/yourusername/web/backend`
6. Reload web app

**Note:** Free tier has limitations on external API calls and socket connections.

---

### Option 3: Heroku

1. Install Heroku CLI
2. Create `Procfile`:
```
web: cd web/backend && gunicorn app:app
```

3. Create `requirements.txt`:
```bash
pip freeze > requirements.txt
```

4. Deploy:
```bash
heroku login
heroku create sosa-services
git push heroku main
```

---

### Option 4: Railway.app (Modern, Easy)

1. Sign up at https://railway.app
2. Connect your GitHub repository
3. Railway auto-detects Python and installs dependencies
4. Set environment variables in dashboard
5. Deploy automatically on push

---

### Option 5: Render.com (Free Tier Available)

1. Sign up at https://render.com
2. Create new Web Service
3. Connect repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `cd web/backend && gunicorn app:app`
6. Deploy

---

## Post-Deployment Checklist

- [ ] Change secret key in config.py
- [ ] Update Telegram bot credentials
- [ ] Configure domain name
- [ ] Setup SSL certificate
- [ ] Test all functionality
- [ ] Setup database backups
- [ ] Configure firewall rules
- [ ] Monitor application logs
- [ ] Setup error tracking (Sentry, etc.)
- [ ] Test payment integration
- [ ] Verify email notifications work

## Security Recommendations

1. **Never commit sensitive data** (API keys, passwords) to version control
2. Use environment variables for secrets
3. Enable HTTPS only
4. Implement rate limiting
5. Regular security updates
6. Use strong passwords for admin accounts
7. Implement CSRF protection
8. Sanitize user inputs
9. Regular database backups
10. Monitor for suspicious activity

## Monitoring

Consider setting up:
- Uptime monitoring (UptimeRobot, Pingdom)
- Error tracking (Sentry)
- Analytics (Google Analytics)
- Server monitoring (New Relic, Datadog)

## Support

For issues or questions, refer to Flask documentation:
- https://flask.palletsprojects.com/
- https://flask-sqlalchemy.palletsprojects.com/
