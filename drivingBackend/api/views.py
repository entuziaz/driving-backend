from django.shortcuts import render
from .models import Question, Option, Course, Feature, Customer
from .serializers import QuestionSerializer, OptionSerializer, CourseSerializer, FeatureSerializer, CustomerSerializer
from rest_framework import generics

from django.conf import settings  # new
from django.http.response import JsonResponse  # new
from django.views.decorators.csrf import csrf_exempt  # new

import time
import stripe

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
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
