# Docker

## Build & run
- Build: `docker compose build`
- Run: `docker compose up`

App will be on http://localhost:8000/

## Notes
- Set AWS credentials and SES region env vars in docker-compose.yml.
- SNS webhook endpoint is http://<host>:8000/ses/
