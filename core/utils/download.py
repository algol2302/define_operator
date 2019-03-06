import sys
import requests
import pathlib


def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')
        print('Начинаем загрузку файла {}'.format(url))
        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(
                    chunk_size=max(int(total/1000), 1024*1024)
            ):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                # прогресс бар самый простой
                # TODO можно использовать progress или tqdm
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

    return 0


def download_files():
    download_tmp_folder = '/tmp/define_operator/'
    pathlib.Path(download_tmp_folder).mkdir(parents=True, exist_ok=True)

    # TODO пока что хардкодим, но далее можно использовать пакет constance,
    #  чтобы определять ссылки через админку
    urls = {
        'https://rossvyaz.ru/data/ABC-3xx.csv': download_tmp_folder +
                                                'ABC-3xx.csv',
        'https://rossvyaz.ru/data/ABC-4xx.csv': download_tmp_folder +
                                                'ABC-4xx.csv',
        'https://rossvyaz.ru/data/ABC-8xx.csv': download_tmp_folder +
                                                'ABC-8xx.csv',
        'https://rossvyaz.ru/data/ABC-9xx.csv': download_tmp_folder +
                                                'ABC-9xx.csv',
    }

    for url, file in urls.items():
        print(url, file)

        res = download(url, file)
        if res == 0:
            pass
        else:
            print('Файл загружен с ошибками! Останавливаем работу...')
