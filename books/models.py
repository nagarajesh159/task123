from django.db import models

from rest_framework import serializers
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    pages = models.IntegerField()

    def __str__(self):
        return self.name


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"