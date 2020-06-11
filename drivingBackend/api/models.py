from django.db import models
from django.contrib.postgres.fields import ArrayField
# import Array field peculiar to PostGres to store array options and features
# from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Question(models.Model):
    name = models.CharField(max_length=25)
    desc = models.CharField(max_length=225)
    typeOfQuestion = models.CharField(max_length=25)
    step = models.IntegerField()
    options = models.ManyToManyField('Option', related_name='+')

    def __str__(self):
        return self.name


class Option(models.Model):
    question = models.ForeignKey(
        Question, verbose_name='Question', on_delete=models.CASCADE)
    desc = models.CharField(max_length=255, blank=False,
                            help_text="Enter an option you want displayed", verbose_name="Option")
    score = models.IntegerField()
    endpoint = models.BooleanField(blank=False, default=False,)

    def __str__(self):
        return self.desc


class Course(models.Model):
    desc = models.TextField()
    transType = models.CharField(max_length=225)
    days = models.IntegerField()
    hours = models.IntegerField()
    fee = models.DecimalField(max_digits=6, decimal_places=2)
    deposit = models.DecimalField(max_digits=6, decimal_places=2)
    # features = models.ManyToManyField('Feature')
    # features = ArrayField(models.CharField(max_length=10, blank=True),size=8)
    features = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.desc


# class Feature(models.Model):
#     course = models.ForeignKey(
#         Course, verbose_name='Courses', on_delete=models.CASCADE)
#     desc = models.CharField(max_length=255, blank=False,
#                             help_text="Enter a feature the user would enjoy by taking the course", verbose_name="Option")


class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    startdate = models.DateField(auto_now=False, auto_now_add=False)
    transType = models.CharField(max_length=50)
    coursechosen = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname
