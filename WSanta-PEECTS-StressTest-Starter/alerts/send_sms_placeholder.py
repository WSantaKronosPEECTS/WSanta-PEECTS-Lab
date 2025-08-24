
# Placeholder for email-to-SMS alerts.
# Configure a mail sender in your infra and deliver to the carrier gateway address.
# Example: 1234567890@txt.att.net (AT&T). Keep secrets out of the repo.

def send_sms(subject: str, body: str, to_gateway: str):
    print(f"[SMS to {to_gateway}] {subject}: {body}")
