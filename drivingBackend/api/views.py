import json
import stripe
import time
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import requests
from django.conf import settings
from django.shortcuts import render, redirect

from .models import Question, Option, Course, Feature, Customer
from .serializers import QuestionSerializer, OptionSerializer, CourseSerializer, FeatureSerializer, CustomerSerializer
from rest_framework import generics
from django.shortcuts import render

from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view


import logging
logger = logging.getLogger(__name__)


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    name = 'question-list'


class OptionList(generics.ListCreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    name = 'option-list'


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    name = 'course-list'


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-list'


class QuestionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class OptionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()


class CourseView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class FeatureView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()


@csrf_exempt
@parser_classes([JSONParser])
def createIntent(request):
    stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY
    #l_data = JSONParser().parse(request)

    if request.method == 'POST':
        # print(request.body)

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(body_data)
        amount = body_data['amount']
        print(amount)
        currency = body_data['currency']
        description = body_data['description']

        # print(request.body)

        # amountGotten = request.POST.get("amount"),
        # print(amountGotten)
        # currency = request.POST.get('currency'),

        # description = request.POST.get('description'),

        # logger.info(description)

        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency=currency,
            description=description,
            # source=request.POST.get('token'),
            # capture=request.POST.get('capture'),

            # Verify integration
            metadata={'integration_check': 'accept_a_payment'},
        )
        try:
            return JsonResponse({'publishableKey':	'your test publishable key', 'clientSecret': intent.client_secret})

        except Exception as e:
            return JsonResponse({'the error na': str(e)}, status=403)
