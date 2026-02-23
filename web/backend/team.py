from flask import render_template, session
from config import app
from utils import dated_url_for

@app.route('/team')
def team():
    user_id = session.get('user_id')
    
    return render_template(
        'team.html',
        user_id=user_id,
        dated_url_for=dated_url_for
    )
