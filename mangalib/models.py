from django.db import models


"""
    primary_key
    unique
    default
    null
    blank

    ChargeField
    IntegerField
    DateField
    EamilField
    BooleanField
"""
class Author(models.Model):
    authore_name = models.CharField(max_length = 64, unique = True)

class Book(models.Model):
    book_title = models.CharField(max_length = 32, unique = True)
    book_quantity = models.IntegerField(default = 1)
    author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)