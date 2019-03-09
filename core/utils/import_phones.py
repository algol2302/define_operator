import csv
import sys
import time

from django.conf import settings

from ..models import (
    DownloadData, Operator,
    Region, PhoneNumber
)

PATH_MEDIA = settings.MEDIA_ROOT + '/download/'


def import_file(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader, None)
        for row in reader:
            # print(row_raw)
            # time.sleep(10)
            # row = row_raw[0].split(';')

            try:
                operator, op_created = Operator.objects.get_or_create(
                    name=row[4].rstrip().lstrip()
                )
            except Exception as e:
                print(f'Error in operator. Row {row}! Exception: {e}')
                sys.exit()

            try:
                reg_col = row[5].rstrip().lstrip()
            except Exception as e:
                print(f'Error in row[5]. Row {row}! Exception: {e}')
                sys.exit()

            try:
                reg_parent = reg_col.split('|')[1].rstrip().lstrip()
            except:
                reg_parent = None
                reg_name = reg_col
            else:
                reg_name = reg_col.split('|')[0].rstrip().lstrip()

            region, reg_created = Region.objects.get_or_create(
                parent=reg_parent,
                name=reg_name
            )

            phone_number, ph_num_created = PhoneNumber.objects.get_or_create(
                abc=int(row[0].rstrip().lstrip()),
                start_number=int(row[1].rstrip().lstrip()),
                end_number=int(row[2].rstrip().lstrip()),
                region=region,
                operator=operator
            )


def import_phones():
    download_data = DownloadData.objects.last()

    # вначале дропаем всю бд, вариант так себе, но пока так
    Region.objects.all().delete()
    Operator.objects.all().delete()
    PhoneNumber.objects.all().delete()
    # TODO импорт сделать более быстрым
    #  оптимизировать выделение диапазонов телефонов у операторов
    import_file(settings.MEDIA_ROOT + '/' + download_data.abc3.name)
    import_file(settings.MEDIA_ROOT + '/' + download_data.abc4.name)
    import_file(settings.MEDIA_ROOT + '/' + download_data.abc8.name)
    import_file(settings.MEDIA_ROOT + '/' + download_data.def9.name)

    return 0
