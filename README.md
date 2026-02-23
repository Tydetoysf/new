# Sosa Services - E-Commerce Platform

A Flask-based e-commerce platform for digital products and services.

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Install required dependencies:
```bash
pip install flask flask-sqlalchemy flask-socketio python-telebot
```

2. Navigate to the backend directory:
```bash
cd web/backend
```

3. Initialize the database:
```bash
python database.py
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:8888`

## Configuration

Edit `web/backend/config.py` to configure:
- Database settings
- Telegram bot integration
- Upload folders
- Session settings

## Project Structure

```
web/
├── backend/          # Flask application and routes
├── static/           # CSS and JavaScript files
├── static2/          # Images and SVG assets
├── templates/        # HTML templates
└── instance/         # Database files
```

## Features

- User authentication (login/register)
- Product management
- Purchase system
- Support ticket system
- Admin panel
- Real-time notifications via Socket.IO
- Telegram integration for notifications

## Security Notes

- Change the secret key in `config.py` before deployment
- Update Telegram bot credentials
- Configure proper database backups
- Use HTTPS in production
- Set up proper firewall rules

## Deployment

For production deployment:
1. Use a production WSGI server (gunicorn, uWSGI)
2. Set up a reverse proxy (nginx, Apache)
3. Configure SSL certificates
4. Use a production database (PostgreSQL, MySQL)
5. Set `debug=False` in app.py

## License

Private project - All rights reserved
