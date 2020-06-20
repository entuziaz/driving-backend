from django.db import models

# import Array field peculiar to PostGres to store array options and features
# from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Question(models.Model):
    name = models.CharField(max_length=25)
    desc = models.CharField(max_length=225)
    typeOfQuestion = models.CharField(max_length=25)
    step = models.IntegerField()
    # options = models.ManyToManyField('Option', related_name='+')
    # options = models.ForeignKey('Option', related_name='+')

    def __str__(self):
        return self.name
        # return self.id, self.name, self.desc, self.typeOfQuestion, self.step


class Option(models.Model):
    question = models.ForeignKey(
        Question, related_name='options', on_delete=models.CASCADE)
    desc = models.CharField(max_length=255, blank=False,
                            help_text="Enter an option you want displayed", verbose_name="Option")
    transType = models.CharField(max_length=20, blank=True)
    score = models.IntegerField()
    endpoint = models.BooleanField(blank=False, default=False,)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.desc
        # return self.id, self.desc, self.score, self.endpoint


class Course(models.Model):
    desc = models.TextField()
    courseType = models.CharField(max_length=40, null=True)
    transType = models.CharField(max_length=225)
    days = models.IntegerField()
    hours = models.IntegerField()
    fee = models.DecimalField(max_digits=6, decimal_places=2)
    deposit = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.desc


class Feature(models.Model):
    course = models.ForeignKey(
        Course, related_name='features', on_delete=models.CASCADE)
    desc = models.CharField(
        max_length=255, help_text="Enter a feature you want displayed",  blank=False, verbose_name="Feature")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.desc
        # return '{} {} {}'.format(self.id, self.desc)


class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    transType = models.CharField(max_length=50)
    courseChosen = models.CharField(max_length=50)

    def __str__(self):
        return self.email
