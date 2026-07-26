# MindsThatMatter Skills Directory

This directory contains modular skill files that document setup procedures, configurations, and solutions for the MindsThatMatter project.

## Available Skills

### Core Setup
- **[environment-setup.md](./environment-setup.md)** - Complete development environment setup
  - System requirements
  - Python virtual environment
  - Dependency installation
  - Database initialization
  - Troubleshooting common setup issues

- **[start-backend.md](./start-backend.md)** - Backend server startup guide
  - Prerequisites and dependencies
  - Virtual environment activation
  - Environment configuration
  - Starting in development or production mode
  - Port requirements and verification

### Documentation & Learning
- **[capture-insights.md](./capture-insights.md)** - Template for documenting complex problem solutions
  - Root cause analysis format
  - Command documentation
  - Configuration and prerequisites
  - Prevention strategies

## Using These Skills

### For Developers
1. **First time setup**: Start with `environment-setup.md`
2. **Starting development**: Follow `start-backend.md`
3. **Encountering issues**: Check troubleshooting sections

### For Agents/Copilot
1. **When solving problems**: Use `capture-insights.md` template
2. **When documenting**: Create new insight files in `../insights/`
3. **When referencing**: Link back to relevant skills

## Skill Structure

Each skill file contains:
- **Overview** - Purpose and scope
- **Prerequisites** - What must be installed/configured first
- **Step-by-step instructions** - Clear, numbered steps
- **Commands** - Copy-paste ready commands in code blocks
- **Port requirements** - Services and their ports
- **Verification** - How to confirm success
- **Troubleshooting** - Common issues and solutions
- **Related skills** - Links to other relevant skills

## Insights Directory

Complex problem solutions are captured in `.github/insights/` directory:
- Named by date and problem: `YYYY-MM-DD-problem-name.md`
- Follows the template in `capture-insights.md`
- Includes root cause analysis
- Documents all discovered commands and configs
- Provides prevention strategies for future reference

## Contributing Skills

When creating a new skill:

1. **Use the standard format**
   - Start with Overview and Prerequisites
   - Include step-by-step instructions
   - Provide copy-paste commands in code blocks
   - Add troubleshooting section

2. **Follow naming convention**
   - Use kebab-case: `skill-name.md`
   - Be descriptive but concise

3. **Include metadata**
   - Link related skills
   - Note any port requirements
   - List all prerequisites and versions

4. **Update this README**
   - Add entry under appropriate category
   - Include brief description (1-2 lines)
   - Link to the skill file

## Quick Reference

| Skill | Purpose | Time | Difficulty |
|-------|---------|------|------------|
| environment-setup.md | Initial dev environment | 10-15 min | Easy |
| start-backend.md | Launch API server | 2-5 min | Easy |
| capture-insights.md | Document solutions | Varies | Medium |

## Port Map

| Port | Service | Skill |
|------|---------|-------|
| 5000 | Flask API | start-backend.md |
| 3000 | Frontend (if applicable) | - |
| 5432 | PostgreSQL (if applicable) | - |

## Support & Issues

If a skill is outdated or unclear:
1. Check the related `../insights/` for recent updates
2. Open an issue with tag `[skill-docs]`
3. Include: OS, Python version, and error encountered

---

**Last Updated**: 2026-07-26  
**Skills Version**: 1.0.0