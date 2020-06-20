from django.shortcuts import render
from .models import Question, Option, Course, Feature, Customer
from .serializers import QuestionSerializer, OptionSerializer, CourseSerializer, FeatureSerializer, CustomerSerializer
from rest_framework import generics

from django.shortcuts import render, redirect
from django.conf import settings  # new
from django.http.response import JsonResponse  # new
from django.views.decorators.csrf import csrf_exempt  # new

import time
import stripe
import json

# Create your views here.


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
def stripe_config(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

        stripe.api_key = settings.STRIPE_PUBLISHABLE_KEY

        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=2044,
            currency='gbp',
            # Verify integration
            metadata={'integration_check': 'accept_a_payment'},
        )

    try:
        return JsonResponse({'publishableKey':	'your test publishable key', 'clientSecret': intent.client_secret})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=403)
