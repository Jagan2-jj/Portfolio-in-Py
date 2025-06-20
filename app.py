import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secret-key-here")

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
    # Sample projects data - in a real application, this might come from a database
    projects_data = [
        {
            'title': 'E-Commerce Platform',
            'description': 'A full-stack e-commerce solution built with Flask and PostgreSQL, featuring user authentication, product catalog, shopping cart, and payment integration.',
            'tech_stack': ['Python', 'Flask', 'PostgreSQL', 'Bootstrap', 'JavaScript'],
            'github_link': 'https://github.com/username/ecommerce-platform',
            'demo_link': 'https://demo-ecommerce.example.com'
        },
        {
            'title': 'Data Visualization Dashboard',
            'description': 'Interactive dashboard for data analysis using D3.js and Chart.js, with real-time data updates and responsive design.',
            'tech_stack': ['JavaScript', 'D3.js', 'Chart.js', 'Python', 'Flask API'],
            'github_link': 'https://github.com/username/data-dashboard',
            'demo_link': 'https://dashboard-demo.example.com'
        },
        {
            'title': 'Task Management App',
            'description': 'A collaborative task management application with user roles, project organization, and real-time notifications.',
            'tech_stack': ['React', 'Node.js', 'MongoDB', 'Socket.io', 'Material-UI'],
            'github_link': 'https://github.com/username/task-manager',
            'demo_link': 'https://tasks-demo.example.com'
        },
        {
            'title': 'Machine Learning Model API',
            'description': 'RESTful API serving machine learning models for predictive analytics with comprehensive documentation and testing suite.',
            'tech_stack': ['Python', 'FastAPI', 'Scikit-learn', 'Docker', 'PostgreSQL'],
            'github_link': 'https://github.com/username/ml-api',
            'demo_link': 'https://ml-api.example.com/docs'
        },
        {
            'title': 'Portfolio Website',
            'description': 'Professional portfolio website built with Flask, featuring responsive design, contact form, and content management system.',
            'tech_stack': ['Python', 'Flask', 'Bootstrap', 'JavaScript', 'SQLite'],
            'github_link': 'https://github.com/username/portfolio',
            'demo_link': 'https://portfolio.example.com'
        }
    ]
    return render_template('projects.html', projects=projects_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Basic validation
        if not all([name, email, subject, message]):
            flash('Please fill in all fields.', 'error')
        else:
            # In a real application, you would send the email here
            # For now, we'll just show a success message
            flash(f'Thank you {name}! Your message has been received. I\'ll get back to you soon.', 'success')
            return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
