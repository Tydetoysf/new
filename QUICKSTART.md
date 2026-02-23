# Sosa Services - Quick Start Guide

## Get Running in 5 Minutes

### Windows Users

1. **Double-click `start.bat`**
   - This will automatically set up everything
   - Wait for "Starting Sosa Services..." message
   - Open browser to `http://localhost:8888`

### Mac/Linux Users

1. **Run the start script:**
```bash
chmod +x start.sh
./start.sh
```

2. **Open browser to:** `http://localhost:8888`

---

## Manual Setup (If Scripts Don't Work)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Initialize Database
```bash
cd web/backend
python database.py
```

### Step 3: Start Application
```bash
python app.py
```

### Step 4: Open Browser
Navigate to: `http://localhost:8888`

---

## First Time Setup

### 1. Create Your First Account
- Click "Register" in the top right
- Fill in username, email, password
- Click "Create Account"

### 2. Make Yourself Admin (Optional)
Stop the server (Ctrl+C) and run:

```bash
cd web/backend
python
```

Then in Python shell:
```python
from database import db, User
from config import app

with app.app_context():
    user = User.query.filter_by(username='YOUR_USERNAME').first()
    user.admin = True
    user.seller = True
    db.session.commit()
    print("Admin access granted!")
```

Exit Python (Ctrl+D or `exit()`) and restart the server.

### 3. Configure Telegram (Optional)
Edit `web/backend/config.py`:
- Get bot token from @BotFather on Telegram
- Get your chat ID from @userinfobot
- Update the values in config.py

### 4. Add Your First Product
- Login with your admin account
- Go to Profile → My Products
- Click "Create Product"
- Fill in details and upload images
- Set price and stock quantity
- Click "Create"

---

## Common Issues

### "Port 8888 already in use"
Change the port in `web/backend/app.py`:
```python
socketio.run(app, host='0.0.0.0', port=8889, debug=True)
```

### "Module not found" errors
Make sure you installed dependencies:
```bash
pip install -r requirements.txt
```

### Database errors
Delete and recreate the database:
```bash
rm web/instance/users.db
cd web/backend
python database.py
```

### Can't access from other devices
Change `host='0.0.0.0'` in app.py and access via your computer's IP address

---

## Next Steps

1. **Customize Branding** - See `CONFIGURATION_GUIDE.md`
2. **Deploy to Production** - See `DEPLOYMENT_GUIDE.md`
3. **Add Products** - Use the admin panel
4. **Configure Payments** - Set up NowPayments API
5. **Test Everything** - Before going live!

---

## Default Features

✅ User registration and authentication
✅ Product catalog with images
✅ Shopping cart and checkout
✅ Support ticket system
✅ Admin panel for management
✅ Real-time notifications
✅ Telegram integration
✅ Responsive design
✅ User profiles and avatars
✅ Order history

---

## Need Help?

- Check `README.md` for project overview
- See `CONFIGURATION_GUIDE.md` for detailed settings
- Read `DEPLOYMENT_GUIDE.md` for hosting options
- Review `PRODUCTS_PLACEHOLDER.md` for product examples

---

## Important Notes

⚠️ **Before Going Live:**
1. Change the secret key in `config.py`
2. Update Telegram credentials
3. Set up proper database (PostgreSQL/MySQL)
4. Enable HTTPS
5. Configure payment processing
6. Test all functionality thoroughly
7. Set `debug=False` in production

⚠️ **Security:**
- Never commit sensitive data to version control
- Use environment variables for secrets
- Keep dependencies updated
- Regular backups
- Monitor for suspicious activity

---

## Quick Commands Reference

```bash
# Start application
python web/backend/app.py

# Reset database
rm web/instance/users.db && cd web/backend && python database.py

# Install dependencies
pip install -r requirements.txt

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Check Python version
python --version

# Update pip
pip install --upgrade pip
```

---

Enjoy using Sosa Services! 🚀
