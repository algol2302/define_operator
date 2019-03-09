from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# from django.shortcuts import HttpResponseRedirect
# from django.urls import reverse
# from django.shortcuts import get_object_or_404
# from shurl.settings import SITE_URL
#
# from .models import *
from .api.viewsets import define_operator_n_region


class PhoneNumber(forms.Form):
    number = forms.RegexField(regex=r'^[7][0-9]\d{9}$', label="Номер")


def index(request):
    phone_number_form = PhoneNumber()

    number = None
    operator = None
    region = None
    error_message = None

    if request.method == "POST":

        number = request.POST.get("number")

        response = define_operator_n_region(number)

        if response['result'] == 'error':
            error_message = response['error_message']
        else:
            operator = response['data']['operator']
            region = response['data']['region']

        return render(
            request, "define_operator.html",
            {
                "form": phone_number_form,
                "number": number,
                "operator": operator,
                "region": region,
                "error_message": error_message,
            },
        )
    else:
        return render(request, "define_operator.html", {"form": phone_number_form})
