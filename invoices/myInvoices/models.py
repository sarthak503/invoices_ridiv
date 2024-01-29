from django.db import models
class Invoice(models.Model):
    date=models.DateField()
    customerName=models.CharField(max_length=255)

class InvoiceDetail(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    description=models.CharField(max_length=255)
    quantity=models.PositiveIntegerField()
    unitPrice=models.DecimalField(max_digits=12,decimal_places=2 )
    price=models.DecimalField(max_digits=12,decimal_places=2 )