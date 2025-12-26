import os
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'laziness_hub_ultra_secret'

# Official Mail Server Configuration
app.config.update(
    MAIL_SERVER='smtp.zoho.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='no.reply@westniles.com',
    MAIL_PASSWORD='Nakintu@1977',
    MAIL_DEFAULT_SENDER='no.reply@westniles.com'
)

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_name = request.form.get('name')
        msg_body = request.form.get('message')

        # Notification to Mbale Prince
        msg_to_me = Message(f"New Hub Inquiry: {user_name}", recipients=['mbaleprince29@gmail.com'])
        msg_to_me.body = f"Client: {user_name}\nEmail: {user_email}\n\nMessage:\n{msg_body}"
        
        # Confirmation to Client
        msg_to_user = Message("Project Received - Westniles Software Hub", recipients=[user_email])
        msg_to_user.body = f"Hello {user_name},\n\nWe have received your inquiry. Our team at Laziness Hub will review your requirements and get back to you shortly.\n\nRegards,\nMbale Prince\ninfo@westniles.com"

        try:
            mail.send(msg_to_me)
            mail.send(msg_to_user)
            flash("Message sent! Protocol initiated.", "success")
        except:
            flash("Network error. Please use WhatsApp.", "danger")
            
    return render_template('index.html', year=datetime.now().year)

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.static_folder, 'sitemap.xml')
