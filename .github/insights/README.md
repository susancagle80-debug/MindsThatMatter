# Insights Index

This directory contains documented insights from complex problem-solving sessions. Each file captures what was learned, including root cause analysis, discovered commands, prerequisites, and prevention strategies.

## How This Works

When agents encounter and solve complex environment or setup problems, they:
1. Use the template in `../skills/capture-insights.md`
2. Create a new file: `YYYY-MM-DD-problem-name.md`
3. Document all insights discovered
4. Reference in related skill files
5. Update this index

## Current Insights

| Date | Problem | Severity | Status | Related Skill |
|------|---------|----------|--------|---------------|
| 2026-07-26 | Backend Startup & Port Alignment | Low | Resolved | .github/skills/start-backend.md |

## Search by Tag

- **backend**: Backend-related issues and solutions
- **frontend**: Frontend-related issues and solutions
- **database**: Database configuration and migration
- **deployment**: Deployment and production issues
- **port-conflict**: Port and network issues
- **dependency**: Dependency and package issues
- **configuration**: Configuration and environment issues
- **development**: Development environment setup
- **performance**: Performance optimization insights
- **docker**: Docker and containerization issues

## File Naming Convention

Format: `YYYY-MM-DD-problem-name.md`

Examples:
- `2026-07-26-backend-startup-port-alignment.md`
- `2026-07-20-database-migration-failure.md`
- `2026-07-15-missing-environment-variables.md`

## Viewing Insights

### By Date (Newest First)
```bash
ls -t *.md
```

### By Problem Type
```bash
grep -l "tags:" *.md | xargs grep -h "tags:" | sort | uniq -c
```

### Full Text Search
```bash
grep -r "root cause\|solution\|command" . --include="*.md"
```

## Using Insights

### For Developers
- Check if your problem was already solved
- Learn from documented root causes
- Apply discovered commands and configurations

### For Agents
- Reference when solving similar problems
- Link to related insights in newly captured problems
- Update general skills based on patterns in insights

## Integration with Skills

Insights inform skill updates:
- If an insight appears frequently, merge it into a skill file
- If a skill becomes outdated, create an insight explaining the change
- Cross-reference between insights and skills

## Archive Policy

Insights are kept indefinitely but can be:
- **Superseded**: If a better solution is found, create new insight and note the old one
- **Merged**: If insights become part of standard skills, archive to `_archive/`
- **Referenced**: Link to similar previous insights to show recurring patterns

---

**Last Updated**: 2026-07-26  
**Total Insights**: 1  
**Tags in Use**: 10
