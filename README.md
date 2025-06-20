# Personal Portfolio Website

A professional Flask-based personal portfolio website with animated borders, dark theme, and responsive design.

## Features

- **Multi-page Design**: Home, About, Projects, and Contact pages
- **Animated Borders**: Beautiful gradient and pulse animations
- **Dark Theme**: Professional Bootstrap dark theme
- **Responsive**: Works perfectly on all devices
- **Contact Form**: Functional contact form with validation
- **Modern UI**: Clean, professional design with smooth animations

## Quick Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package installer)

### Installation Steps

1. **Extract the project files**
   ```bash
   unzip portfolio-website.zip
   cd portfolio-website
   ```

2. **Install Python dependencies**
   ```bash
   pip install flask flask-sqlalchemy gunicorn psycopg2-binary email-validator
   ```

3. **Set environment variables** (optional)
   ```bash
   export SESSION_SECRET="your-secret-key-here"
   ```

4. **Run the application**
   
   **For Development:**
   ```bash
   python main.py
   ```
   
   **For Production:**
   ```bash
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   ```

5. **Open your browser**
   - Navigate to `http://localhost:5000`
   - The website will be running locally

## Project Structure

```
portfolio-website/
├── app.py              # Main Flask application with routes
├── main.py             # Application entry point
├── pyproject.toml      # Project dependencies
├── templates/          # HTML templates
│   ├── base.html       # Base template with navigation
│   ├── home.html       # Home page with hero section
│   ├── about.html      # About page with bio and skills
│   ├── projects.html   # Projects showcase
│   └── contact.html    # Contact form and information
├── static/             # Static assets
│   ├── css/
│   │   └── style.css   # Custom CSS with animations
│   └── assets/
│       └── profile-placeholder.svg  # Profile image
└── README.md           # This file
```

## Customization

### Update Personal Information

1. **Edit templates** to replace placeholder content:
   - Update name, bio, and contact details
   - Modify project descriptions and links
   - Change social media links

2. **Replace profile image**:
   - Add your photo to `static/assets/`
   - Update the image path in `templates/home.html`

3. **Customize colors** in `static/css/style.css`:
   - Modify CSS variables for colors
   - Adjust animation speeds and effects

### Add New Projects

Edit the `projects_data` list in `app.py`:

```python
projects_data.append({
    'title': 'Your Project Name',
    'description': 'Project description...',
    'tech_stack': ['Python', 'Flask', 'JavaScript'],
    'github_link': 'https://github.com/username/project',
    'demo_link': 'https://your-demo.com'
})
```

## Deployment Options

### Heroku
1. Create a `Procfile`:
   ```
   web: gunicorn main:app
   ```
2. Deploy using Heroku CLI

### Replit
- The project is ready to deploy on Replit
- Just click the "Deploy" button in Replit

### Other Platforms
- Works with any platform supporting Python/Flask
- Set PORT environment variable if required

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5, Custom CSS
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)
- **Server**: Gunicorn (production)

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

MIT License - feel free to use this template for your own portfolio!

## Support

If you encounter any issues:
1. Check that all dependencies are installed
2. Verify Python version compatibility
3. Ensure port 5000 is available
4. Check the console for error messages

---

**Enjoy your new portfolio website!** 🚀