from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_discount_html_email(user_email, context):
    """
    Sends an HTML email to a user.
    context = {
        'patient_name': "",
        'patient_email': "",
        'patient_phone': "",
        'discount_range': "",
        'reference_id': "",
        'request_date': "",
        'hospital_name': "",
        'hospital_phone': "",
        'support_email': "",
        'terms_url': "",
        'call_to_action_url': "",
        'hospital_address': "",
    }
    """

    subject = f"Thank you for contacting {context.get('hospital_name')}"

    # Renders templates/discount_email.html with variables
    html_content = render_to_string("discount_email.html", context)

    send_mail_to_email(settings.DEFAULT_FROM_EMAIL, settings.DEFAULT_FROM_EMAIL,  html_content, "A lead Genrated")
    send_mail_to_email(settings.DEFAULT_FROM_EMAIL, user_email,  html_content, subject)
    
    
        

def send_mail_to_email(email, email_to,  html_content, subject):
    email = EmailMessage(
        subject=subject,
        body=html_content,
        from_email=email,
        to=[email_to],
    )

    # Tell Django the body is HTML
    email.content_subtype = "html"

    email.send(fail_silently=False)