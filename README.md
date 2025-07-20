# 📞 Contact Manager

A full-stack Contact Management application built with Django REST Framework backend and Streamlit frontend, featuring JWT-based authentication and secure API endpoints.

## ✨ Features

- **🔐 JWT Token Authentication** - Secure login with access and refresh tokens
- **📝 Contact Management** - Create, view, and manage contacts via REST API
- **🛡️ Secured Endpoints** - All contact operations require authentication
- **👨‍💼 Admin Panel** - Django admin interface for contact data management
- **🖥️ Modern Frontend** - Interactive Streamlit web interface
- **📱 Responsive Design** - Clean, user-friendly contact forms and displays

## 🚀 Tech Stack

### Backend
- **Django** - Web framework
- **Django REST Framework** - API development
- **djangorestframework-simplejwt** - JWT authentication
- **SQLite** - Database (easily replaceable with PostgreSQL)

### Frontend
- **Streamlit** - Python-based web UI framework

## 📁 Project Structure

```
contact-manager/
├── contacts/                    # Django app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py              # Contact model
│   ├── serializers.py         # DRF serializers
│   ├── views.py               # API views
│   └── urls.py                # API endpoints
├── contact_mgmt/               # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── streamlit_app/
│   └── app.py                 # Streamlit frontend
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd contact-manager
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Django Backend
```bash
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start Django development server
python manage.py runserver
```
Backend will be available at `http://127.0.0.1:8000/`

### 5. Launch Streamlit Frontend
```bash
# In a new terminal (with virtual environment activated)
streamlit run streamlit_app/app.py
```
Frontend will be available at `http://localhost:8501/`

## 🔑 Authentication Flow

### 1. Obtain JWT Tokens
```bash
POST /api/token/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 2. Use Access Token
Include the access token in the Authorization header:
```bash
Authorization: Bearer <access_token>
```

### 3. Refresh Token
When access token expires:
```bash
POST /api/token/refresh/
Content-Type: application/json

{
    "refresh": "your_refresh_token"
}
```

## 📚 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/token/` | Obtain JWT tokens | ❌ |
| POST | `/api/token/refresh/` | Refresh access token | ❌ |
| POST | `/api/register/` | User registration | ❌ |
| GET | `/api/contacts/` | List all contacts | ✅ |
| POST | `/api/contacts/` | Create new contact | ✅ |
| GET | `/api/contacts/{id}/` | Get specific contact | ✅ |
| PUT | `/api/contacts/{id}/` | Update contact | ✅ |
| DELETE | `/api/contacts/{id}/` | Delete contact | ✅ |

## 💡 Usage Examples

### Creating a Contact
```bash
POST /api/contacts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1234567890"
}
```

### Retrieving Contacts
```bash
GET /api/contacts/
Authorization: Bearer <access_token>
```

## 🖥️ Streamlit Interface

The Streamlit frontend provides:

1. **Login Screen** - Authenticate users and obtain JWT tokens
2. **Contact Creation Form** - Add new contacts with validation
3. **Contact Dashboard** - View and manage existing contacts
4. **Logout Functionality** - Secure session management

### Key Features:
- Session state management for authentication
- Form validation and error handling
- Real-time API integration
- Responsive layout and user-friendly interface

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

### Database Configuration
To use PostgreSQL instead of SQLite, update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'contact_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🛡️ Security Features

- JWT-based authentication with access and refresh tokens
- Password hashing using Django's built-in authentication
- CORS configuration for frontend-backend communication
- Input validation and sanitization
- Secure API endpoints with authentication requirements

## 🚀 Deployment

### Backend (Django)
- Use Gunicorn for production WSGI server
- Configure PostgreSQL for production database
- Set up static file serving
- Configure environment variables

### Frontend (Streamlit)
- Deploy using Streamlit Cloud
- Configure API base URL for production
- Set up environment variables for production

## ScreenShot

#### Registration/Login
<img width="1919" height="893" alt="Screenshot 2025-07-20 202653" src="https://github.com/user-attachments/assets/7a0ea2d2-c2d3-4ab4-8519-afce1b0a083f" />
<img width="1919" height="944" alt="Screenshot 2025-07-20 202643" src="https://github.com/user-attachments/assets/9c880de4-ff20-47be-8068-8a3ed83a680f" />

#### View Content(CRUD Function)
<img width="1915" height="1017" alt="image" src="https://github.com/user-attachments/assets/3d24c472-6de1-4906-91f2-069c28b0c90e" />
<img width="1914" height="1030" alt="Screenshot 2025-07-20 212822" src="https://github.com/user-attachments/assets/99aec8bb-9c87-4b97-9da7-dc2dcd7f5f7f" />

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License

## 📞 Support

If you have any questions or issues, please open an issue on GitHub or contact the maintainers.
Developer- Abhay Tiwari


---

**Happy Contact Managing! 📞✨**
