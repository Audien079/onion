import datetime
import requests
from admin import logger
from celery import shared_task
from report.models import Website


@shared_task
def check_status():
    """
    Checks status of all websites
    """
    websites = Website.objects.all()

    for website in websites:
        response = requests.get(website, timeout=5)
        status_code = response.status_code
        if status_code == 200:
            website.status = True
            website.last_active = datetime.datetime.now()
        else:
            website.status = False

        website.status_code = status_code
        website.last_check = datetime.datetime.now()
        website.save()
        logger.info(f"Checked status for {website}")

    logger.info("Fetched status for all the websites")


@shared_task
def test_celery():
    for i in range(20):
        print(i, ' ooooop ', i)
