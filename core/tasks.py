from defop import celery_app


@celery_app.task
def start_download():
    from .utils.download import download_files
    return download_files()


@celery_app.task
def start_import():
    from .utils.import_phones import import_phones
    return import_phones()
