from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=10, null=True)
    price = models.IntegerField(null=True)
    firma = models.ForeignKey(Company, on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    pack = models.CharField(max_length=10, null=True)
    recomend = models.BooleanField(null=True)


class Course(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=10)
    group = models.CharField(max_length=4)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

