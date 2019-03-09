import sys
import requests
import pathlib
import filecmp
from shutil import copyfile

from django.conf import settings

from ..models import DownloadData
PATH_MEDIA = settings.MEDIA_ROOT + '/download/'


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
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

    return 0


def create_download_data(download_tmp_folder):
    pathlib.Path(PATH_MEDIA).mkdir(parents=True, exist_ok=True)
    copyfile(
        download_tmp_folder + 'ABC-3xx.csv', PATH_MEDIA + 'ABC-3xx.csv'
    )
    copyfile(
        download_tmp_folder + 'ABC-4xx.csv', PATH_MEDIA + 'ABC-4xx.csv'
    )
    copyfile(
        download_tmp_folder + 'ABC-8xx.csv', PATH_MEDIA + 'ABC-8xx.csv'
    )
    copyfile(
        download_tmp_folder + 'DEF-9xx.csv', PATH_MEDIA + 'DEF-9xx.csv'
    )
    created_data = DownloadData.objects.create()
    created_data.abc3.name = DownloadData.DOWNLOAD_DIRECTORY + 'ABC-3xx.csv'
    created_data.abc4.name = DownloadData.DOWNLOAD_DIRECTORY + 'ABC-4xx.csv'
    created_data.abc8.name = DownloadData.DOWNLOAD_DIRECTORY + 'ABC-8xx.csv'
    created_data.abc9.name = DownloadData.DOWNLOAD_DIRECTORY + 'DEF-9xx.csv'
    created_data.save()

    return created_data


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
        'https://rossvyaz.ru/data/DEF-9xx.csv': download_tmp_folder +
                                                'DEF-9xx.csv',
    }

    for url, file in urls.items():
        print(url, file)

        res = download(url, file)
        if res == 0:
            pass
        else:
            print(f'Файл {file} загружен с ошибками!')
            sys.exit()

    # нужно проверить если ли такие файлы в бд
    #  если нет, то создать запись

    last_data = DownloadData.objects.last()

    if last_data:
        res3 = filecmp.cmp(
            download_tmp_folder + 'ABC-3xx.csv',
            settings.MEDIA_ROOT + '/' + last_data.abc3.name
        )
        res4 = filecmp.cmp(
            download_tmp_folder + 'ABC-4xx.csv',
            settings.MEDIA_ROOT + '/' + last_data.abc4.name
        )
        res8 = filecmp.cmp(
            download_tmp_folder + 'ABC-8xx.csv',
            settings.MEDIA_ROOT + '/' + last_data.abc8.name
        )
        res9 = filecmp.cmp(
            download_tmp_folder + 'DEF-9xx.csv',
            settings.MEDIA_ROOT + '/' + last_data.abc9.name
        )

        # делаем самую простую проверку, если хотя бы один из файлов отличается
        # то дропаем всю базу

        if res3 and res4 and res8 and res9:
            return 0
        else:
            last_data.delete()
            created_data = create_download_data(download_tmp_folder)
    else:
        created_data = create_download_data(download_tmp_folder)

    return created_data
