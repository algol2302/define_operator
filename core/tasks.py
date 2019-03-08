from defop import celery_app


@celery_app.task
def start_download():
    from .utils.download import download_files
    res = download_files()
    # проверяем нужно ли обновлять бд телефонов
    if res == 0:
        return res
    else:
        from .utils.import_phones import import_phones
        import_phones()

    return res
