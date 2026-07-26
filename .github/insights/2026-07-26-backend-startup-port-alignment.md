---
date: 2026-07-26
problem: "Backend Startup & Port Alignment"
severity: "low"
resolution_time: "20 minutes"
agent: "Copilot"
tags: ["backend", "port-conflict", "development", "docker"]
---

# Insight: Backend Startup & Port Alignment

## Problem Statement
- Initializing the backend without local mock dependencies running caused runtime errors
- Port collision issues when services weren't started in correct order
- `.env` configuration was missing, causing connection failures to Redis and Mock API

## Root Cause Analysis
The backend service depends on:
1. **Redis** - Caching layer (port 6379)
2. **Mock API** - Local service simulation (port 8080)
3. **Database** - Persistence layer (configurable port)

These services must start before the Flask development server attempts to connect, otherwise connection timeouts and port conflicts occur.

## Solution Details

### Commands Discovered
```bash
# Proper startup sequence
docker-compose up -d database redis
sleep 5  # Wait for services to be ready
npm run dev  # Or: flask run

# Individual service startup
docker-compose up -d redis
docker-compose up -d database
docker-compose up -d mock-api

# Verify services are running
docker-compose ps
netstat -an | grep -E '6379|8080|5000'

# Check service logs
docker-compose logs redis
docker-compose logs database
docker-compose logs mock-api
```

### Configuration Requirements
- `.env` file must be created from `.env.example` **before** service startup
- Key configuration for backend:
  - `REDIS_URL=redis://localhost:6379`
  - `DATABASE_URL=sqlite:///mindsthatmatter.db` or `postgresql://user:pass@localhost:5432/db`
  - `MOCK_API_URL=http://localhost:8080`
  - `API_PORT=5000`

### Port Requirements
| Service | Port | Environment Variable | Purpose |
|---------|------|----------------------|---------|
| Flask Backend | 5000 | `API_PORT` | Development API server |
| Redis | 6379 | `REDIS_PORT` | Caching and session storage |
| Mock API | 8080 | `MOCK_API_PORT` | Local dependency simulation |
| Database | 5432 (PostgreSQL) or 3306 (MySQL) | `DATABASE_URL` | Data persistence |

### Prerequisites
- Docker 20.10+
- Docker Compose 1.29+
- Python 3.8+
- Node.js 14+ (if using npm)
- Virtual environment activated

### Environment Variables
```
# .env.local (copy from .env.example)
REDIS_URL=redis://localhost:6379
REDIS_PORT=6379
DATABASE_URL=sqlite:///db.sqlite3
MOCK_API_URL=http://localhost:8080
MOCK_API_PORT=8080
API_PORT=5000
DEBUG=True
FLASK_ENV=development
LOG_LEVEL=DEBUG
```

## Implementation Steps

1. **Copy environment file**
   ```bash
   cp .env.example .env.local
   ```

2. **Verify docker-compose.yml exists**
   - Check that Redis, Database, and Mock API services are defined
   - Ensure correct ports are mapped

3. **Start infrastructure services first**
   ```bash
   docker-compose up -d database redis mock-api
   ```

4. **Wait for services to be ready** (5-10 seconds)
   ```bash
   sleep 10
   docker-compose ps  # Verify all containers are "Up"
   ```

5. **Activate Python virtual environment**
   ```bash
   source venv/bin/activate
   ```

6. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

7. **Start Flask development server**
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

8. **Verify all services connected**
   - Backend responds: `curl http://localhost:5000/health`
   - Check Redis connection: `curl http://localhost:5000/health/redis`
   - Check Mock API connection: `curl http://localhost:5000/health/mock-api`

## Verification Checklist
- [ ] All Docker containers running: `docker-compose ps` shows all "Up"
- [ ] No port conflicts: `netstat -an` shows ports 5000, 6379, 8080 in use
- [ ] `.env.local` file exists with correct values
- [ ] Flask starts without connection errors
- [ ] Health check endpoints respond successfully
- [ ] Backend logs show successful connections to Redis and Mock API

## Prevention Strategies

1. **Automate startup sequence**
   - Create shell script: `scripts/start-dev.sh`
   - Execute: `docker-compose up -d && sleep 10 && flask run`
   - Add to project README

2. **Add pre-commit hooks**
   - Verify `.env.local` exists before committing
   - Check docker-compose syntax on hook trigger

3. **Document in onboarding**
   - Add startup sequence to CONTRIBUTING.md
   - Include troubleshooting section in main README
   - Link to this insight document

4. **Add health check to Makefile**
   ```makefile
   .PHONY: health
   health:
   	@echo "Checking backend health..."
   	@curl http://localhost:5000/health
   	@echo "\nChecking Redis..."
   	@curl http://localhost:5000/health/redis
   	@echo "\nChecking Mock API..."
   	@curl http://localhost:5000/health/mock-api
   ```

## Common Issues & Solutions

### Issue: "Cannot connect to Redis at localhost:6379"
```bash
# Solution: Start Redis
docker-compose up -d redis
docker-compose logs redis  # Check for errors
```

### Issue: "Port 6379 already in use"
```bash
# Solution: Kill existing Redis or use different port
docker-compose down
docker-compose up -d redis
# Or modify port in docker-compose.yml
```

### Issue: "Mock API returning 503 Service Unavailable"
```bash
# Solution: Ensure Mock API container started first
docker-compose up -d mock-api
sleep 5
docker-compose logs mock-api
```

### Issue: "Address already in use :5000"
```bash
# Solution: Check what's using port 5000
lsof -i :5000
kill -9 <PID>
# Or use different port
flask run --port=5001
```

## Performance Impact
- **Startup time**: +10 seconds (waiting for Docker services)
- **Memory usage**: +500MB (Redis + Mock API containers)
- **CPU usage**: Minimal after startup (< 5% per service at idle)

## Related Skills & Documentation
- `.github/skills/start-backend.md` - Backend startup guide (parent skill)
- `.github/skills/environment-setup.md` - Initial environment setup
- `.github/skills/capture-insights.md` - Template for documenting insights

## Timeline & Debugging Steps
1. Encountered Flask connection timeout errors
2. Discovered backend code expects Redis on port 6379
3. Found docker-compose.yml was incomplete/outdated
4. Updated compose file with all required services
5. Added .env template with correct connection strings
6. Tested service startup sequence multiple times
7. Documented execution order as critical prerequisite

## Notes
- Services must start in dependency order (databases first, then app)
- Docker network allows services to communicate via container names (no localhost needed within containers)
- Health check endpoints are critical for development workflow validation
- Consider using docker-compose override files for different environments (dev, test, staging)

---

**Created:** 2026-07-26  
**Last Updated:** 2026-07-26  
**Status:** Resolved & Documented