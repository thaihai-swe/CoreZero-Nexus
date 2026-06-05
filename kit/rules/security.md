# Security Rules

- Never log or output plain-text credentials, tokens, or passwords.
- Treat external or user input as untrusted: validate and sanitize before using.
- Do not execute raw OS commands constructed from external strings without strict validation.
- Review all dependencies against known CVEs before introducing them.
