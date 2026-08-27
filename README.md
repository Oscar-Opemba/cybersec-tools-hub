# CyberSec Interactive Tools

A public collection of small, interactive defensive cybersecurity utilities. Each tool is a standalone Python repository with a localhost web interface, a CLI where appropriate, tests, and explicit authorization boundaries.

## Tool directory

| Tool | What it does | Repository |
| --- | --- | --- |
| HTTP Security Headers Checker | Reviews common response headers for one URL | [http-security-headers-checker](https://github.com/Oscar-Opemba/http-security-headers-checker) |
| TLS Certificate Inspector | Inspects certificate identity, expiry, and negotiated protocol | [tls-certificate-inspector](https://github.com/Oscar-Opemba/tls-certificate-inspector) |
| DNS Security Checker | Reviews A, AAAA, MX, TXT, SPF, DMARC, and CAA records | [dns-security-checker](https://github.com/Oscar-Opemba/dns-security-checker) |
| Password Strength Checker | Estimates passphrase quality offline | [password-strength-checker](https://github.com/Oscar-Opemba/password-strength-checker) |
| JWT Decoder | Decodes claims locally and flags review signals | [jwt-decoder](https://github.com/Oscar-Opemba/jwt-decoder) |
| Phishing URL Analyzer | Scores URL signals without visiting the link | [phishing-url-analyzer](https://github.com/Oscar-Opemba/phishing-url-analyzer) |
| Local Secret Scanner | Finds likely secrets with redacted output | [secret-scanner](https://github.com/Oscar-Opemba/secret-scanner) |
| File Integrity Checker | Calculates and verifies SHA-256/SHA-512 | [file-integrity-checker](https://github.com/Oscar-Opemba/file-integrity-checker) |
| Authentication Log Analyzer | Summarizes failed-login patterns from local logs | [auth-log-analyzer](https://github.com/Oscar-Opemba/auth-log-analyzer) |
| OSV Dependency Scanner | Looks up one package version in OSV | [osv-dependency-scanner](https://github.com/Oscar-Opemba/osv-dependency-scanner) |
| CORS Policy Checker | Reviews one endpoint’s preflight response | [cors-policy-checker](https://github.com/Oscar-Opemba/cors-policy-checker) |
| CIDR Subnet Calculator | Calculates network ranges offline | [subnet-calculator](https://github.com/Oscar-Opemba/subnet-calculator) |
| security.txt Checker | Validates one site’s disclosure contact file | [security-txt-checker](https://github.com/Oscar-Opemba/security-txt-checker) |

## Why these tools

The projects target practical defensive searches such as HTTP security headers checker, TLS certificate checker, DNS security checker, JWT decoder, phishing URL analyzer, secret scanner, SHA-256 file checker, failed-login analyzer, OSV dependency scanner, CORS checker, CIDR calculator, and security.txt checker. They are intentionally small enough to inspect end to end and safe enough to run locally.

## Market-readiness documentation

The collection’s acceptance criteria, trust model, package contracts, release checklist, and residual-risk guidance are summarized in [MARKET_READINESS.md](MARKET_READINESS.md). Each standalone repository also contains its own [API_CONTRACT.md](https://github.com/Oscar-Opemba/http-security-headers-checker/blob/main/API_CONTRACT.md), release checklist, changelog, and hardening guide.

## Safety boundary

This collection does not provide payload generation, persistence, credential attacks, exploit delivery, evasion, process injection, port scanning, domain fronting, or automated interaction with third-party targets. Network tools make one bounded request to the exact target entered by the user and require authorization. Offline tools keep their inputs local.

## References

- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/)
- [Qualys SSL Labs SSL Server Test](https://www.ssllabs.com/ssltest/)
