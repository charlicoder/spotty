from typing import Any
from django.db import models

GENDER = {
    "M": "Male",
    "F": "Femalte",
    "O": "Other"
}


class Author(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    gender = models.CharField(max_length=10, choices=GENDER, blank=False, null=False)
    about = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    series_name = models.CharField(max_length=100, blank=True, null=True)
    average_rating = models.FloatField(default=0.0, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class BookAuthors(models):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     role = models.CharField(max_length=100, blank=True, null=True)
#     publication_date = models.DateField(default=None, blank=True, null=True)
