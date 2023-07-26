from django.db import models

class Purchase(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    quantity = models.PositiveIntegerField(default=1)
    # Add other fields as needed

    def __str__(self):
        return f"{self.id}: {self.product_name} - {self.purchase_date}"