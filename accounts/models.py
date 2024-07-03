from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Account(models.Model):
    account_number = models.IntegerField(unique=True)
    account_name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0,validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_name} ({self.account_number}) - Balance: {self.balance} {self.currency}"


