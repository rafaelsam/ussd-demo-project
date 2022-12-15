from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        service_code = request.POST.get('service_code')
        phone_number = request.POST.get('phone_number')
        text = request.POST.get('text')

        response = ""
        if text == "":
            response = "CON Welcome to our Subscription services \n"
            response += "1. Sport \n"
            response += "2. Political \n"
            response += "3. Local \n"
            response += "4. Internation"

        elif text == "1":
            response = "CON Select your Sport plan \n"
            response += "1. Daily 100Tsh \n"
            response += "2. Weekly 500Tsh \n"
            response += "3. Monthly 2000Tsh"

        elif text == "1*1":
            response = "CON You will be charged 100Tsh for your daily sports news subscription"
            response += "1. Auto renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*1*1":
            response = "END thank you for subscribing to our daily sport news plan \n"

        elif text == "1*1*2":
            response = "END thank you for your one-off daily sport news plan \n"

        elif text == "1*2":
            response = "CON You will be charged 500Tsh for our weekly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*2*1":
            response = "END thank you for subscribing to our weekly sport news plan \n"

        elif text == "1*2*2":
            response = "END thank you for your one-off weekly sport news plan \n"

        elif text == "1*3":
            response = "CON You will be charged 2000Tsh for our monthly Sports news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"

        elif text == "1*3*1":
            response = "END thank you for subscribing to our monthly sport news plan \n"

        elif text == "1*3*2":
            response = "END thank you for your one-off monthly sport news plan \n"
            
        return HttpResponse(response)

