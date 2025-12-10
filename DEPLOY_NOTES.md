Deployment notes - Let's Encrypt & SMS provider

1) Let's Encrypt (automated via nginx-proxy + acme-companion)
- Edit docker-compose.prod.yml: replace example.com and admin@example.com with your actual domain and email.
- Ensure domain DNS A record points to server IP.
- Run: docker compose -f docker-compose.prod.yml up -d
- acme-companion will request certs from Let's Encrypt automatically.

2) SMS provider configuration
- Twilio: set env vars TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM (phone number with country code)
- Or use a generic HTTP provider: set SMS_HTTP_ENDPOINT and SMS_HTTP_APIKEY
- In dev, OTP code is returned in response (ENV!=prod). In prod, code is not returned and SMS must be delivered.