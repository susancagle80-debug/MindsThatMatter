# Capture Insights Template

This template is used to document complex environment setups, configurations, and solutions discovered during agent problem-solving sessions.

## Instructions for Agents

When you solve a complex environment or setup problem:
1. Fill out this template with the insights gained
2. Save it to `.github/insights/[date]-[problem-name].md`
3. Reference in related skill files
4. Update the insights index

---

## Template

```yaml
---
date: YYYY-MM-DD
problem: "Brief problem statement"
severity: "critical|high|medium|low"
resolution_time: "Duration to resolve"
agent: "Agent name/ID"
tags: ["tag1", "tag2"]
---

# Insight: [Problem Name]

## Problem Statement
- What issue was encountered?
- What was broken or not working?
- How did it affect development?

## Root Cause Analysis
- What was the underlying cause?
- Why did this happen?
- What conditions triggered it?

## Solution Details

### Commands Discovered
\`\`\`bash
# List exact commands that solved the issue
command 1
command 2
command 3
\`\`\`

### Configuration Requirements
- Setting 1: Explanation
- Setting 2: Explanation
- Setting 3: Explanation

### Port Requirements
- Service: Port (why this port)
- Service: Port (why this port)

### Prerequisites
- Prerequisite 1 (version if applicable)
- Prerequisite 2 (version if applicable)
- Prerequisite 3 (version if applicable)

### Environment Variables
\`\`\`
VAR_NAME=value # Purpose
VAR_NAME2=value # Purpose
\`\`\`

## Implementation Steps
1. Step 1 with explanation
2. Step 2 with explanation
3. Step 3 with explanation

## Verification
How to confirm the solution works:
- [ ] Check 1
- [ ] Check 2
- [ ] Check 3

## Prevention
How to prevent this issue in the future:
- Prevention strategy 1
- Prevention strategy 2
- Prevention strategy 3

## Related Skills & Documentation
- Link to skill file
- Link to documentation
- Related issue #123

## Performance Impact
- Any performance implications?
- Resource usage changes?
- Scalability considerations?

## Notes
- Any additional context or caveats
- Edge cases to watch for
- Future improvements

## Learned From
- Stack traces or error messages
- Environment details (OS, Python version, etc.)
- Timeline of debugging steps
```

---

## Example Insight Entry

```yaml
---
date: 2026-07-26
problem: "Flask app failing to start due to port conflict on development machine"
severity: "high"
resolution_time: "15 minutes"
agent: "Copilot"
tags: ["backend", "port-conflict", "development"]
---

# Insight: Resolving Flask Port Conflict on Development Machine

## Problem Statement
- Flask development server failed to start on port 5000
- Error: "Address already in use"
- Blocked all local API development

## Root Cause Analysis
- Previous Flask instance wasn't properly terminated
- Process still holding the port in TIME_WAIT state
- Development workflow didn't include cleanup steps

## Solution Details

### Commands Discovered
\`\`\`bash
# Identify process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>

# Or use this one-liner
lsof -ti:5000 | xargs kill -9

# Verify port is free
lsof -i :5000
\`\`\`

### Port Requirements
- Flask Dev: 5000 (configurable)
- Debug: 5001 (if debugger enabled)

### Prerequisites
- Python 3.8+
- `pip install flask`

## Implementation Steps
1. Check if port 5000 is in use with `lsof -i :5000`
2. Kill any existing process on that port
3. Wait 5 seconds for OS to release port
4. Start Flask with `flask run`

## Verification
- [ ] `flask run` starts without "Address already in use" error
- [ ] API responds to `curl http://localhost:5000/health`
- [ ] No lsof output for port 5000 after shutdown

## Prevention
- Add port-check script to startup process
- Document proper Flask shutdown procedure
- Use `--port` flag to rotate ports if conflicts occur
- Consider using systemd or supervisor for process management

## Related Skills & Documentation
- `.github/skills/start-backend.md`
- `.github/skills/environment-setup.md`
```