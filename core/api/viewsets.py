from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q
import json

from ..models import (
    PhoneNumber, Operator,
    Region
)


def validation(number):
    return True


def define_operator_n_region(number):

    response = {
        "result": "error",
        "error_message": "Invalid phone format"
    }

    if validation(number):

        raw_number = number
        number_abc = raw_number[1:4]
        start_end_number = raw_number[4:]

        phone_number = PhoneNumber.objects.filter(
            abc=int(number_abc),
            start_number__lte=int(start_end_number),
            end_number__gte=int(start_end_number),
        ).first()
        if phone_number:
            operator = phone_number.operator.name
            region_parent = phone_number.region.parent
            region_name = phone_number.region.name
            region = region_parent + " " + region_name if region_parent \
                else region_name

            response = {
                "result": "success",
                "data": {
                    "operator": operator,
                    "region": region
                }
            }

    return response


class PhoneNumberAPI(ViewSet):
    def retrieve(self, request, pk, format=None):

        res = define_operator_n_region(pk)

        if res['result'] == 'success':
            return Response(res, status=status.HTTP_200_OK)
        elif res['result'] == 'error':
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
