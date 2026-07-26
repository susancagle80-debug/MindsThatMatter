# Start Backend Skill

## Overview
Instructions for starting the backend server for the MindsThatMatter application.

## Prerequisites
- Python 3.8+
- Virtual environment (`venv`)
- Dependencies installed via `pip install -r requirements.txt`

## Setup Commands

### 1. Activate Virtual Environment
```bash
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the project root with:
```
FLASK_ENV=development
FLASK_APP=app.py
DATABASE_URL=sqlite:///mindsthatmatter.db
API_PORT=5000
```

## Starting the Backend

### Development Mode
```bash
flask run --host=0.0.0.0 --port=5000
```

### Production Mode
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Port Requirements
- **Backend API**: `5000` (configurable via `API_PORT` env var)
- **Database**: SQLite local (or remote if configured)

## Verification
- Health check: `curl http://localhost:5000/health`
- API docs: `http://localhost:5000/api/docs`

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
# Or use a different port
flask run --port=8000
```

### Missing Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Database Issues
```bash
# Reset database
rm mindsthatmatter.db
flask db init
flask db migrate
flask db upgrade
```

## Related Skills
- Environment setup
- Database migration
- API testing