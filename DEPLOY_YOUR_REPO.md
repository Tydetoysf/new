# 🚀 Deploy Your Sosa Services Website

## ✅ Your Code is on GitHub!

**Repository:** https://github.com/Tydetoysf/new

Your website is now backed up and ready to deploy publicly!

---

## 🌐 Deploy to Railway.app (Recommended - 5 Minutes)

### Step 1: Go to Railway
Visit: https://railway.app

### Step 2: Sign In
- Click "Login"
- Choose "Login with GitHub"
- Authorize Railway to access your GitHub

### Step 3: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose "Tydetoysf/new" from the list
4. Click "Deploy Now"

### Step 4: Configure Environment Variables
1. In Railway dashboard, click on your project
2. Go to "Variables" tab
3. Add these variables:
   - `SECRET_KEY`: Generate with `python -c "import secrets; print(secrets.token_hex(32))"`
   - `TELEGRAM_BOT_TOKEN`: Your bot token (optional)
   - `TELEGRAM_CHAT_ID`: Your chat ID (optional)

### Step 5: Get Your URL
- Railway will automatically deploy
- Click "Settings" → "Generate Domain"
- Your site will be live at: `https://your-app.up.railway.app`

**Done!** Your website is now public! 🎊

---

## 🆓 Deploy to Render.com (Free Tier)

### Step 1: Go to Render
Visit: https://render.com

### Step 2: Sign In with GitHub
- Click "Get Started"
- Sign in with GitHub
- Authorize Render

### Step 3: Create Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub account
3. Select "Tydetoysf/new" repository
4. Click "Connect"

### Step 4: Configure
- **Name:** sosa-services
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `cd web/backend && gunicorn --worker-class eventlet -w 1 app:app`
- **Plan:** Free

### Step 5: Add Environment Variables
Click "Advanced" and add:
- `SECRET_KEY`: Generate a random string
- `TELEGRAM_BOT_TOKEN`: (optional)
- `TELEGRAM_CHAT_ID`: (optional)

### Step 6: Deploy
- Click "Create Web Service"
- Wait for deployment (5-10 minutes)
- Your site will be live at: `https://sosa-services.onrender.com`

**Done!** Free hosting! 🎉

---

## ⚡ Deploy with Railway CLI (Fastest)

If you have Node.js installed:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link to your GitHub repo
railway link

# Deploy
railway up
```

**Done in 2 minutes!**

---

## 🔧 Important: Update Configuration

Before your site goes live, update these in `web/backend/config.py`:

### 1. Change Secret Key
```python
# Generate new key:
python -c "import secrets; print(secrets.token_hex(32))"

# Then update in config.py:
app.secret_key = "YOUR_NEW_SECRET_KEY_HERE"
```

### 2. Set Debug to False
```python
# In web/backend/app.py, change:
socketio.run(app, host='0.0.0.0', port=8888, debug=False)
```

### 3. Update Telegram (Optional)
```python
app.config['TELEGRAM_BOT'] = "YOUR_BOT_TOKEN"
app.config['TELEGRAM_CHAT_ID'] = YOUR_CHAT_ID
```

Then commit and push:
```bash
git add .
git commit -m "Update configuration for production"
git push
```

Railway/Render will auto-deploy the changes!

---

## 📱 After Deployment

Once deployed, you can:

1. **Visit your public URL**
   - Railway: `https://your-app.up.railway.app`
   - Render: `https://sosa-services.onrender.com`

2. **Test everything:**
   - Create an account
   - Browse products
   - Check team page: `/team`
   - Test all features

3. **Share your URL!**
   - Your website is now live on the internet
   - Anyone can access it

4. **Add custom domain (optional):**
   - Both Railway and Render support custom domains
   - Configure in platform settings

---

## 🎯 Recommended Next Steps

1. ✅ Deploy on Railway (easiest)
2. ✅ Update secret key and configuration
3. ✅ Test your live site
4. ✅ Add team photos to `web/static/images/team/`
5. ✅ Update social media links
6. ✅ Add real products
7. ✅ Share your URL!

---

## 🆘 Troubleshooting

### Deployment Failed?
- Check Railway/Render logs
- Verify `requirements.txt` is correct
- Make sure `Procfile` exists
- Check Python version in `runtime.txt`

### Site Not Loading?
- Wait 5-10 minutes for first deployment
- Check platform status page
- Review deployment logs
- Verify start command is correct

### Database Issues?
- SQLite works for testing
- For production, add PostgreSQL database
- Railway/Render offer database add-ons

---

## 💰 Pricing

**Railway:**
- $5 free credit per month
- Then ~$5-10/month
- Best performance

**Render:**
- Free tier available
- Free tier sleeps after inactivity
- Paid plans from $7/month

---

## 🎊 You're Almost Live!

Your code is on GitHub: https://github.com/Tydetoysf/new

**Choose your platform:**
- **Want easiest?** → Railway.app
- **Want free?** → Render.com
- **Want fastest?** → Railway CLI

**Follow the steps above and your site will be live in minutes!** 🚀

---

## 📞 Support

- Railway Docs: https://docs.railway.app
- Render Docs: https://render.com/docs
- Your Guides: Check all .md files in your repo

**Ready to deploy? Pick a platform and go!** 🌐
