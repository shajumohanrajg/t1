from django.core.mail import EmailMessage
# from django.conf import settings

import logging

logging = logging.getLogger(__name__)


class Util:
    @staticmethod
    def send_email(data):
        try:
            email = EmailMessage(
                subject=data['email_subject'],
                body=data["email_body"],
                to=[data['to_email']]
            )

            if data.get("email_body_html"):
                email.content_subtype = 'html'
                email.body = data['email_body_html']

            # if data.get("attachments"):
            #     for attachment in data["attachments"]:
            #         email.attach(attachment['filename'],attachment['content'],attachment['mimetype'])

            email.send()
            logging.info(f"Email sent successfully to{data['to_email']}")

        except Exception as e:
            logging.error(f"An error occurred while sending email to {data['to_email']}:{e}")
            raise
