import logging
from .celery import app as celery_app


__all__ = ("celery_app",)

logger = logging.getLogger(__name__)
