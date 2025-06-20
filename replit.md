# Personal Portfolio Website

## Overview

This is a Flask-based personal portfolio website designed to showcase a developer's skills, projects, and professional information. The application features a clean, modern interface with dark theme styling and responsive design. It's built using Python Flask as the backend framework with Bootstrap for frontend styling.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5 with custom dark theme
- **Icons**: Font Awesome 6.4.0
- **Typography**: Google Fonts (Inter family)
- **Responsive Design**: Mobile-first approach with Bootstrap grid system

### Backend Architecture
- **Framework**: Flask 3.1.1 (Python web framework)
- **Application Structure**: Simple MVC pattern
- **Entry Point**: `main.py` serves as the application entry point
- **Core Logic**: `app.py` contains route definitions and application configuration
- **Session Management**: Flask's built-in session handling with secret key configuration

### Data Storage Solutions
- **Current State**: Static data stored in Python dictionaries within route handlers
- **Database Ready**: Dependencies include Flask-SQLAlchemy and psycopg2-binary for future PostgreSQL integration
- **Prepared for Scaling**: Architecture supports easy migration to database-driven content

## Key Components

### Core Application Files
1. **`main.py`** - Application entry point and development server configuration
2. **`app.py`** - Main Flask application with route definitions, logging setup, and sample data
3. **`pyproject.toml`** - Project dependencies and metadata using modern Python packaging standards

### Template Structure
- **`templates/base.html`** - Base template with navigation, Bootstrap integration, and common layout
- **`templates/home.html`** - Landing page with hero section and skills showcase
- **`templates/about.html`** - Personal information, education, and professional background
- **`templates/projects.html`** - Portfolio projects display with tech stack and links
- **`templates/contact.html`** - Contact form for visitor inquiries

### Static Assets
- **`static/css/style.css`** - Custom CSS with CSS variables, transitions, and responsive enhancements
- **`static/assets/profile-placeholder.svg`** - Animated SVG placeholder for profile image

## Data Flow

1. **Request Routing**: Flask handles incoming HTTP requests and routes them to appropriate view functions
2. **Template Rendering**: Jinja2 processes templates with context data (projects, personal info)
3. **Static Content**: Flask serves CSS, images, and other static assets
4. **Form Processing**: Contact form submissions are handled server-side with Flash messaging
5. **Response Generation**: HTML responses are generated and returned to the client

## External Dependencies

### Python Packages
- **Flask 3.1.1**: Core web framework
- **Flask-SQLAlchemy 3.1.1**: Database ORM (prepared for future use)
- **psycopg2-binary 2.9.10**: PostgreSQL adapter (prepared for future use)
- **email-validator 2.2.0**: Email validation for contact forms
- **Gunicorn 23.0.0**: WSGI HTTP server for production deployment

### Frontend Dependencies (CDN)
- **Bootstrap 5**: CSS framework with dark theme
- **Font Awesome 6.4.0**: Icon library
- **Google Fonts**: Inter font family for typography

### System Packages (Nix)
- **Python 3.11**: Runtime environment
- **OpenSSL**: Cryptographic library
- **PostgreSQL**: Database system (prepared for future use)

## Deployment Strategy

### Development Environment
- **Local Server**: Flask development server with debug mode and auto-reload
- **Port Configuration**: Application runs on port 5000 with host binding to 0.0.0.0
- **Hot Reloading**: Gunicorn configured with `--reload` flag for development

### Production Deployment
- **WSGI Server**: Gunicorn with autoscale deployment target
- **Process Management**: Multiple worker processes for handling concurrent requests
- **Port Binding**: Production server binds to 0.0.0.0:5000 for external access
- **Environment Variables**: Session secret key configurable via environment variables

### Replit Integration
- **Nix Environment**: Stable channel 24_05 with required system packages
- **Workflow Automation**: Parallel task execution with automatic port detection
- **Module System**: Python 3.11 module with required dependencies

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

- June 20, 2025: Initial portfolio website setup with Flask backend
- June 20, 2025: Added animated gradient borders throughout the website for visual appeal
- June 20, 2025: Created complete deployment package with README and setup instructions

## Changelog

- June 20, 2025: Complete personal portfolio website with animated borders, dark theme, and responsive design
- Created downloadable package with full setup instructions
- Implemented gradient and pulse border animations on hero section, skills cards, projects, and contact form