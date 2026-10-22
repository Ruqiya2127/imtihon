from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.SmallIntegerField(default=1954)
    country = models.CharField(max_length=250)

    def str(self):
        return self.full_name

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_year = models.CharField(max_length=200)
    pages = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def str(self):
        return self.title
