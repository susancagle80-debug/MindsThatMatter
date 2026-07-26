# MindsThatMatter Project Directives

These guidelines are mandatory for all development within the MindsThatMatter project to ensure security, scalability, and maintainability.

## 1. Secrets Management
- **Never commit** raw private keys, API tokens, or secrets to the repository.
- **Development:** Use `.env` files (ignored by git).
- **Staging/Production:** Use secure alternatives: AWS Secrets Manager, HashiCorp Vault, or encrypted environment variables within the deployment pipeline (e.g., GitHub Actions Secrets).

## 2. Skill Validation
- All new or modified skills must pass validation before being merged or considered complete.
- **Command:** `skills-ref validate ./skills/<skill-name>`

## 3. Documentation (SKILL.md)
- **Length Constraint:** Core `SKILL.md` files MUST be under 500 lines.
- **Structure:** Utilize progressive disclosure.
- **References:** Move large code snippets, complex schemas, or extensive documentation blocks into a `references/` subdirectory.

## 4. Deterministic Finality
- Agents must explicitly terminate using a code-based function (e.g., `finalize_task` or `submit_appraisal`) rather than relying on natural language.
