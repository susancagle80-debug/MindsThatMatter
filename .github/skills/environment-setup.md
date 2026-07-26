# Environment Setup Skill

## Overview
Complete guide for setting up the development environment for MindsThatMatter.

## System Requirements
- **OS**: macOS 10.14+, Linux (Ubuntu 18.04+), or Windows 10+
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: 2GB free

## Installation Steps

### 1. Clone Repository
```bash
git clone https://github.com/susancagle80-debug/MindsThatMatter.git
cd MindsThatMatter
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 4. Install Python Dependencies
```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 5. Create Environment Variables File
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
API_PORT=5000
LOG_LEVEL=INFO
```

### 6. Initialize Database
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### 7. Create Admin User (if applicable)
```bash
python manage.py create-admin --email admin@example.com --password admin123
```

## Verification Checklist
- [ ] Python 3.8+ installed: `python --version`
- [ ] Virtual environment active: `which python` shows venv path
- [ ] Dependencies installed: `pip list | grep -E 'flask|sqlalchemy'`
- [ ] `.env` file created and configured
- [ ] Database initialized: SQLite file exists
- [ ] Backend starts: `flask run` runs without errors

## Common Issues & Solutions

### Python Version Mismatch
```bash
# Check version
python3 --version

# If Python 3 not found, install it via Homebrew (macOS)
brew install python3
```

### Permission Denied on venv
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

### Pip SSL Certificate Error
```bash
pip install --trusted-host pypi.python.org -r requirements.txt
```

## Next Steps
- Run start-backend.md skill to launch the API
- See testing guide for running test suite
- Refer to database migration guide for schema updates

## Environment Variables Reference

| Variable | Purpose | Default |
|----------|---------|----------|
| `DEBUG` | Enable debug mode | `False` |
| `SECRET_KEY` | Flask secret key | `dev-key` |
| `DATABASE_URL` | Database connection string | `sqlite:///db.sqlite3` |
| `API_PORT` | Port for API server | `5000` |
| `LOG_LEVEL` | Logging verbosity | `INFO` |