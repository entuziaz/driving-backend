from rest_framework import serializers
from .models import Question, Option, Course, Feature, Customer


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'desc', 'transType', 'score', 'endpoint')


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'name', 'desc', 'typeOfQuestion', 'step', 'options')

    # method below allows write-create/update to work on Option model
    def create(self, validated_data):
        options = validated_data.pop('options')
        question = Question.objects.create(**validated_data)
        for option in options:
            Option.objects.create(question=question, **option_data)
        return question

    def update(self, instance, validated_data):
        options = validated_data.pop('options')
        options = (instance.options).all()
        options = list(options)
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.typeOfQuestion = validated_data.get(
            'typeOfQuestion', instance.typeofQuestion)
        instance.step = validated_data.get('step', instance.step)
        instance.save()

        for option in options:
            option = options.pop(0)
            option.desc = option.get('desc', option.desc)
            option.score = option.get('score', option.score)
            option.endpoint = option.get('endpoint', option.endpoint)
            option.save()
        return instance


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'desc')


# class ListingSerializer(serializers.ModelSerializer):
#     # slug_field should be 'name', i.e. the name of the field on the related model
#     category = serializers.SlugRelatedField(slug_field='name',
#                                             queryset=models.Category.objects.all())
#     ...


class CourseSerializer(serializers.ModelSerializer):
    features = serializers.SlugRelatedField(
        many=True, slug_field='desc', queryset=Feature.objects.all())

    class Meta:
        model = Course
        fields = ('id', 'desc', 'courseType', 'transType', 'days',
                  'hours', 'fee', 'deposit', 'features')

    # method below allows write-create/update to work on Option model
    def create(self, validated_data):
        features = validated_data.pop('features')
        course = Course.objects.create(**validated_data)
        for feature in features:
            Feature.objects.create(course=course, **feature_data)
        return course

    def update(self, instance, validated_data):
        features = validated_data.pop('features')
        features = (instance.features).all()
        features = list(features)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.courseType = validated_data.get(
            'courseType', instance.courseType)
        instance.transType = validated_data.get(
            'transType', instance.transType)
        instance.days = validated_data.get('days', instance.days)
        instance.hours = validated_data.get('hours', instance.hours)
        instance.fee = validated_data.get('fee', instance.fee)
        instance.deposit = validated_data.get('days', instance.deposit)

        instance.save()

        for feature in features:
            feature = features.pop(0)
            feature.desc = feature.get('desc', feature.desc)
            feature.score = feature.get('score', feature.score)
            feature.endpoint = feature.get('endpoint', feature.endpoint)
            feature.save()
        return instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('firstName', 'lastName', 'email', 'phone',
                  'startDate', 'postCode', 'courseChosen')
