# Sosa Services - Configuration Guide

## Basic Configuration

### 1. Application Settings (`web/backend/config.py`)

```python
# Security - CHANGE THIS!
app.secret_key = os.urandom(24)  # Generate new: python -c "import os; print(os.urandom(24))"

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # For production, use PostgreSQL/MySQL

# File Upload Settings
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max upload

# Telegram Integration
app.config['TELEGRAM_BOT'] = "YOUR_BOT_TOKEN_HERE"  # Get from @BotFather
app.config['TELEGRAM_CHAT_ID'] = YOUR_CHAT_ID_HERE  # Your Telegram chat ID

# Cache Control
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(minutes=1)

# Version (for cache busting)
app.config['HTML_VERSION'] = 2.2
```

### 2. Getting Telegram Bot Token

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow instructions to create your bot
4. Copy the token provided
5. Paste into `config.py`

### 3. Getting Telegram Chat ID

Method 1 - Using a bot:
1. Search for `@userinfobot` on Telegram
2. Start the bot
3. It will show your chat ID

Method 2 - Manual:
1. Send a message to your bot
2. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Look for `"chat":{"id":` in the response

### 4. Database Configuration

For production, replace SQLite with PostgreSQL:

```python
# PostgreSQL example
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'

# MySQL example
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
```

## Branding Customization

### 1. Site Name and Description

Edit `web/templates/base.html`:
- Line ~40: Change site title
- Line ~60: Update header text and tagline

Edit `web/templates/index.html`:
- Line ~8: Main page title
- Line ~9: Main page description

### 2. Logo and Images

Replace files in `web/static2/images/`:
- `logo.svg` - Main logo
- `avatar.png` - Default avatar
- `layout.png` - Background image
- `auth_layout.png` - Login/register background

### 3. Colors and Styling

Edit `web/static/css/style.css` to change:
- Primary colors
- Accent colors
- Font styles
- Layout spacing

Common CSS variables to customize:
```css
:root {
    --accent: #your-color;
    --background: #your-color;
    --text-color: #your-color;
}
```

### 4. Social Media Links

Edit `web/templates/base.html` (footer section):
```html
<button onclick="window.open('YOUR_YOUTUBE_URL', '_blank')" class="contact-button youtube"></button>
<button onclick="window.open('YOUR_TELEGRAM_URL', '_blank')" class="contact-button telegram"></button>
<button onclick="window.open('YOUR_DISCORD_URL', '_blank')" class="contact-button discord"></button>
```

## Product Configuration

### Adding Products via Admin Panel

1. Create an admin account:
```python
# In Python shell or script
from database import db, User
from config import app

with app.app_context():
    user = User.query.filter_by(username='your_username').first()
    user.admin = True
    user.seller = True
    db.session.commit()
```

2. Login and access admin panel
3. Create products with:
   - Name
   - Description
   - Price
   - Images
   - Category
   - Stock quantity

### Product Categories

Edit product categories in your admin panel or database:
- Software Tools
- Utilities
- Services
- Digital Products
- Custom category names

## Payment Integration

### NowPayments Setup

1. Sign up at https://nowpayments.io
2. Get your API key
3. Add to user profile in admin panel
4. Configure accepted cryptocurrencies

### Alternative Payment Processors

To integrate other payment systems:
1. Edit `web/backend/purchase.py`
2. Add payment provider API integration
3. Update payment flow in templates

## Email Configuration (Optional)

To add email notifications:

```python
# Add to config.py
from flask_mail import Mail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'

mail = Mail(app)
```

## Security Configuration

### 1. Change Secret Key

```python
# Generate secure key
import secrets
print(secrets.token_hex(32))

# Use in config.py
app.secret_key = 'your-generated-key-here'
```

### 2. Enable HTTPS Only

In production config:
```python
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
```

### 3. Rate Limiting

Install Flask-Limiter:
```bash
pip install Flask-Limiter
```

Add to config:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
```

## Backup Configuration

### Automated Database Backups

Create `backup.sh`:
```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
cp web/instance/users.db backups/users_$DATE.db
# Keep only last 30 days
find backups/ -name "users_*.db" -mtime +30 -delete
```

Add to crontab:
```bash
0 2 * * * /path/to/backup.sh
```

## Environment Variables (Recommended)

For production, use environment variables:

```python
import os

app.config['TELEGRAM_BOT'] = os.environ.get('TELEGRAM_BOT_TOKEN')
app.config['TELEGRAM_CHAT_ID'] = int(os.environ.get('TELEGRAM_CHAT_ID'))
app.secret_key = os.environ.get('SECRET_KEY')
```

Create `.env` file (don't commit to git):
```
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id
SECRET_KEY=your_secret_key
```

## Testing Configuration

Before going live:
1. Test user registration
2. Test login/logout
3. Test product creation
4. Test purchase flow
5. Test ticket system
6. Test admin panel
7. Test on mobile devices
8. Test payment integration
9. Verify Telegram notifications
10. Check all links work

## Troubleshooting

### Database Issues
```bash
# Reset database (WARNING: deletes all data)
rm web/instance/users.db
cd web/backend
python database.py
```

### Port Already in Use
Change port in `app.py`:
```python
socketio.run(app, host='0.0.0.0', port=8889, debug=True)
```

### Static Files Not Loading
Clear browser cache or update HTML_VERSION in config.py

### Telegram Not Working
- Verify bot token is correct
- Check chat ID is a number (not string)
- Ensure bot has permission to send messages
