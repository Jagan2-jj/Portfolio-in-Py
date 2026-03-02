import os
import logging
from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secret-key-here")

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jaganpanigrahi2004@gmail.com'
app.config['MAIL_PASSWORD'] = 'kkhfbtohtnnjslzr'
app.config['MAIL_DEFAULT_SENDER'] = 'jaganpanigrahi2004@gmail.com'

db = SQLAlchemy(app)
mail = Mail(app)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def home():
    """Home page route"""
    return render_template('home.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/projects')
def projects():
    """Projects page route"""
    projects_data = [
        {
            'title': 'LinkLens AI – AI Career Advisor',
            'description': 'LinkLens AI is a full-stack web application built using the MERN stack (JavaScript) with LinkedIn OAuth for secure authentication and automated profile submission. It analyzes LinkedIn profile data to generate a personalized profile score and delivers AI-driven recommendations to improve professional visibility. The platform also includes an ATS resume checker and an interview preparation module providing role-specific career readiness support.',
            'tech_stack': ['MongoDB', 'Express.js', 'React.js', 'Node.js', 'LinkedIn OAuth', 'AI'],
            'github_link': 'https://github.com/Jagan2-jj/LinkLens-AI',
            'demo_link': '#'
        },
        {
            'title': 'IssueSense – Hostel Issue Management App',
            'description': 'IssueSense is a React Native–based mobile application developed to streamline issue management for hostel students. The app allows users to report problems with photo evidence, analyzes and classifies the issues, and sends realtime notifications to the respective warden or service staff such as electricians and plumbers. It also includes an SOS emergency feature to ensure quick response and enhanced student safety.',
            'tech_stack': ['React Native', 'Node.js', 'Express.js', 'MongoDB'],
            'github_link': 'https://github.com/Jagan2-jj/IssueSense',
            'demo_link': '#'
        },
        {
            'title': 'Roll Paradise – Food Ordering Web App',
            'description': 'Food ordering application focused on efficient CRUD operations and smooth API integration for menu management and order processing.',
            'tech_stack': ['Python', 'Flask', 'MongoDB'],
            'github_link': 'https://github.com/Jagan2-jj/Roll-Paradise',
            'demo_link': '#'
        },
        {
            'title': 'Portfolio Application',
            'description': 'A structured backend-driven portfolio application to showcase projects and technical profile. Strengthened understanding of backend logic and web application structure.',
            'tech_stack': ['Python', 'Flask', 'HTML/CSS', 'JavaScript'],
            'github_link': 'https://github.com/Jagan2-jj/Portfolio-in-Py',
            'demo_link': '#'
        }
    ]
    return render_template('projects.html', projects=projects_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling and email notification"""
    if request.method == 'POST':
        # Safely handle both Form and JSON data
        if request.is_json:
            data = request.get_json()
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message_content = data.get('message')
        else:
            name = request.form.get('name')
            email = request.form.get('email')
            subject = request.form.get('subject')
            message_content = request.form.get('message')
        
        # Validation
        if not all([name, email, subject, message_content]):
            if request.is_json:
                return jsonify({"error": "Please fill in all fields"}), 400
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))
        
        try:
            # 1. Save to Database
            new_message = ContactMessage(
                name=name,
                email=email,
                subject=subject,
                message=message_content
            )
            db.session.add(new_message)
            db.session.commit()
            
            # 2. Send Email Notification
            msg = Message(
                subject=f"Portfolio Inquiry: {subject}",
                recipients=['jaganpanigrahi2004@gmail.com'],
                body=f"New Message from {name} ({email}):\n\n{message_content}"
            )
            mail.send(msg)
            
            if request.is_json:
                return jsonify({"success": "Message sent and saved successfully!"}), 200
            
            flash(f'Thank you {name}! Your message has been received and sent to my email.', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            app.logger.error(f"Error handling contact form: {str(e)}")
            if request.is_json:
                return jsonify({"error": "Failed to process your request. Please try again later."}), 500
            flash("There was an error sending your message. Please try again later.", "error")
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
