from appconf import AppConf


class DjangoCeleryEmailAppConf(AppConf):
    class Meta:
        prefix = 'CELERY_EMAIL'

    TASK_CONFIG = {}
    BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    CHUNK_SIZE = 10
    ATTACHMENT_COMPRESSION = None
    MESSAGE_EXTRA_ATTRIBUTES = None
