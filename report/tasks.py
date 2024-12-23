import datetime
import requests
from bs4 import BeautifulSoup
from admin import logger
from celery import shared_task
from report.models import Website
from admin.utils import email_down_sites


@shared_task
def check_status():
    """
    Checks status of all websites
    """
    websites = Website.objects.all()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for website in websites:
        response = requests.get(website, headers=headers, timeout=7)
        status_code = response.status_code
        if status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            if "error" not in title:
                website.status = True
                website.last_active = datetime.datetime.now()
            else:
                website.status = False
        else:
            website.status = False

        website.status_code = status_code
        website.last_check = datetime.datetime.now()
        website.save()
        logger.info(f"Checked status for {website}")

    email_down_sites("andrew.quel@gmail.com")
    email_down_sites("audien079@gmail.com")
    logger.info("Fetched status for all the websites")


@shared_task
def test_celery():
    for i in range(20):
        print(i, ' ooooop ', i)
