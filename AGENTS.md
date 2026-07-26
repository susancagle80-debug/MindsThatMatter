# AGENTS.md

**Purpose:** Define autonomous actions, responsibilities, and reference materials for AI agents working on this repository.

---

## Autonomous Actions (Always Do)

When working on this repository, agents should automatically:

1. **Capture complex solutions**
   - When resolving a non-obvious build or environment failure, log the solution using the template in `.github/skills/capture-insights.md`
   - Append a new entry to `.github/insights/README.md` with the insight details
   - File naming: `YYYY-MM-DD-problem-name.md` in `.github/insights/`

2. **Reference modular skills**
   - When solving setup or configuration issues, check `.github/skills/` first
   - Link to relevant skill files in your documentation
   - If a skill is outdated, create an insight explaining the change

3. **Validate before proceeding**
   - Check `.github/insights/README.md` to see if this problem was already solved
   - Reference previous insights to avoid duplicate work
   - Build upon existing documentation rather than starting from scratch

4. **Update documentation consistency**
   - When creating new skills, ensure they follow the format defined in `.github/skills/README.md`
   - Include all required sections: Overview, Prerequisites, Commands, Port Requirements, Verification, Troubleshooting

5. **Maintain cross-references**
   - Link insights to their related skill files
   - Update skill files when new insights become general patterns
   - Tag insights appropriately for searchability

---

## Skill & Insight References

### Backend Operations

- **Backend Boot:** [`.github/skills/start-backend.md`](.github/skills/start-backend.md)
  - How to start the Flask development server
  - Port requirements and configuration
  - Troubleshooting common startup issues

- **Environment Setup:** [`.github/skills/environment-setup.md`](.github/skills/environment-setup.md)
  - Initial development environment setup
  - Virtual environment creation
  - Dependency installation and database initialization

- **Capture Insights:** [`.github/skills/capture-insights.md`](.github/skills/capture-insights.md)
  - Template for documenting complex problem solutions
  - Used when resolving non-obvious environment or setup issues

### Insights Repository

- **Insights Index:** [`.github/insights/README.md`](.github/insights/README.md)
  - Central index of all captured insights
  - Searchable by date, tag, and problem type
  - Integration guidelines for keeping insights up-to-date

- **Backend Startup Insight:** [`.github/insights/2026-07-26-backend-startup-port-alignment.md`](.github/insights/2026-07-26-backend-startup-port-alignment.md)
  - Detailed walkthrough of backend startup with Docker
  - Port alignment and service dependency order
  - Prevention strategies and common issues

---

## Agent Capabilities & Constraints

### What Agents Can Do

✅ Create new skill files in `.github/skills/` following the standard format  
✅ Create new insight files in `.github/insights/` using the capture template  
✅ Update `.github/insights/README.md` with new insight entries  
✅ Link between skills and insights for cross-referencing  
✅ Modify existing skills to incorporate new insights  
✅ Update this `AGENTS.md` file with new guidelines or reference materials  

### What Agents Should NOT Do

❌ Modify skill templates without consensus  
❌ Delete insight records (archive to `_archive/` instead)  
❌ Create vague or undocumented problem-solving sessions  
❌ Skip creating insights for complex environment problems  
❌ Leave broken or outdated references in documentation  

---

## Workflow: Solving a Complex Problem

When an agent encounters a non-obvious problem:

1. **Investigate & solve** the problem as needed
2. **Document the journey** (commands, root cause, solutions)
3. **Create an insight file** using the template in `.github/skills/capture-insights.md`
4. **Save to `.github/insights/YYYY-MM-DD-problem-name.md`**
5. **Update `.github/insights/README.md`** with new table entry
6. **Reference in related skills** if the insight is broadly applicable

Example: *"Agent encounters Flask port conflict during dev startup"*
- Solves it by killing the old process and documenting the sequence
- Creates: `.github/insights/2026-07-26-flask-port-conflict.md`
- Updates: `.github/insights/README.md` (adds table row)
- References: `.github/skills/start-backend.md` (links to the insight)

---

## Directory Structure

```
.github/
├── skills/
│   ├── README.md                      # Skills directory index
│   ├── capture-insights.md            # Template for capturing insights
│   ├── environment-setup.md           # Initial dev environment
│   ├── start-backend.md               # Backend startup guide
│   └── [other modular skills].md
│
└── insights/
    ├── README.md                      # Insights index & search
    ├── 2026-07-26-backend-startup-port-alignment.md
    ├── [YYYY-MM-DD-problem-name].md
    └── _archive/                      # Superseded or merged insights
```

---

## Quick Links

| Resource | Purpose | Location |
|----------|---------|----------|
| Skills Directory | All modular how-to guides | `.github/skills/` |
| Insights Index | All captured problem solutions | `.github/insights/README.md` |
| Insight Template | Format for new insights | `.github/skills/capture-insights.md` |
| Backend Setup | Start developing locally | `.github/skills/start-backend.md` |
| Environment Setup | First-time environment config | `.github/skills/environment-setup.md` |

---

## Support & Escalation

If you encounter:
- **Unclear documentation**: Update it and note the change in an insight
- **Recurring problems**: Create an insight and consider promoting to a skill
- **Out-of-date references**: Flag in insights with "SUPERSEDED" tag
- **Policy questions**: Update this `AGENTS.md` file to clarify

---

**Last Updated**: 2026-07-26  
**Version**: 1.0.0  
**Repository**: susancagle80-debug/MindsThatMatter
