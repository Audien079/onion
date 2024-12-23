from django.template.loader import render_to_string
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from django.conf import settings
from report.models import Website


def send_email(to_email, subject, html_content):
    """
    Send email using sendgrid
    """
    message = Mail(
        from_email='cody@useexplore.com',
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return response.status_code

    except Exception as e:
        return str(e)


def queryset_to_dict(queryset):
    result = {}
    for obj in queryset:
        result[obj.id] = {
            'name': obj.name,
            'price': obj.price,
        }
    return result


def email_down_sites(to_email):
    """email test"""
    subject = 'Sites Tracker'
    sites = Website.objects.filter(status=False)
    results = []
    for obj in sites:
        results.append(obj.web_url)

    context = {"sites": results}
    html_message = render_to_string("reports/email_downsites.html", context=context)
    send_email(to_email, subject, html_message)
