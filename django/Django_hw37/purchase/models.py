from django.db import models
from book.models import Book

class Purchase(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.book} - {self.purchase_date}"