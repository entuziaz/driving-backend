from django.contrib import admin
from .models import Question, Option, Course, Feature, Customer


admin.site.register(Question)
admin.site.register(Option)

admin.site.register(Course)
admin.site.register(Feature)

admin.site.register(Customer)
