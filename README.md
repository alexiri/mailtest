# Mailtest

Simple Django app to test django-post-office delivery through AWS SES with SNS webhooks.

## Configure
Set at least:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SES_REGION_NAME`

Optional:
- `AWS_SES_CONFIGURATION_SET`
- `AWS_SES_RETURN_PATH`

SNS webhook endpoint:
- `/ses/` (configure in AWS SNS subscription)

## Run
1. Install deps from requirements.txt.
2. Run migrations: `python manage.py migrate`.
3. Start server: `python manage.py runserver`.
4. Visit `/` to send a test email. Admin at `/admin/`.

## Docker
See README.docker.md.
