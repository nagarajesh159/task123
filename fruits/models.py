from django.db import models

# Create your models here.


class Fruit(models.Model):
    grade_choices =(
        ('choose-grade', '----'),
        ('grade1', 'grade1'),
        ('grade2', 'grade2'),
        ('grade3', 'grade3'),
    )

    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=10, choices=grade_choices)

    def __str__(self):
        return self.name +"----" +self.grade
