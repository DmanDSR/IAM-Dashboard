# DevOps Team Scope — IAM Dashboard (Spring 2026)

[REMOTE] Team Meetings: Tuesday 1:00-1:30

# Team Members List (3)
Ahanaf - DevOps Lead
Alvin - DevOps Member
Saleh - DevOps Member (?) 

# OFFICIAL TASK LIST ROAD MAP

# Week 1 February 17 – February 23

    •	Complete scope and ownership document, onboarding all members with docker and git knowledge.
    •	Local environment setup
    •	Docker basics (containers, volumes, networks, etc.)
    •   Fix Docker Healthcheck

This week focuses on infra stability and onboarding process.

# Week 2 February 24 – March 2

Focus: CI/CD & Infra Automation

    •	Fix CI pipeline (Github Actions)
    •   Add Vite Service to Docker for FrontEnd
    •   Add Terraform apply workfrom on merge for infra deployment
    •   Ensure Docker services build cleanly in CI
    •   Improve Docker Image Layering (to optimize build times)
    •   Validate terraform workflow: (apply on merge to main, prevent manual drift)
    •   Add deployment health verification step.

This weeks goal is to have a completely automated & reliable infra pipleline along with better infra stability.

# Week 3 March 3 – March 9

Focus: Email + Local Dev Quality

    •	Add MailHog for local email testing:
        Welcome Email,
        Password Reset,
        Alert Emails
    •   Verify environment variable management (.env)
    •   Ensure local dev mirrors production setup.

This weeks goal is to improve developer experience.  

# Week 4 March 10 – March 16

Focus: Optimization and Security Hardening

    •	Optimize Docker images (reducing size & improve caching)
    •   Implement CI lint/format gates
    •   Verify deployment health endpoints.
    •   Review secrets management (securing terraform variables, and no secrets in repo (important))
    •   Audit IAM permissions, following the least privilege principles.

This weeks goal is to have production-ready reliability and security.

# Week 5 March 17 – March 23

Focus: Data & Governance Support

    •	Support reports and audience backend integrations.
    •   Implement data retention policy infra
    •   Add logging + monitoring improvements
    •   Verify Prometheus/Grafana dashboards.

This weeks goal is to ensure governance compliance and observability.

# Week 6 April 13 - April 17 

Focus: Production Preparation

    •	Infrastructure Stress Testing
    •   Monitoring Alert Tuning
    •   Finalize Documentation for CI/CD flow diagram and onboarding guide.
    •   Final deployment verification.

This weeks goal is to ensure stable, scaleable, and documented infrastructure.





   



