from django.db import models
from django.utils import timezone

class Transfer(models.Model):
    origin_account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='transfers_sent')
    destination_account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='transfers_received')
    date_and_time = models.DateTimeField(default=timezone.now)
    transfer_amount = models.DecimalField(max_digits=12, decimal_places=2)
    transfer_type = models.CharField(max_length=15, blank=True, default='')
    transfer_code = models.CharField(max_length=15, blank=True, default='')
    transfer_charge = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=15, blank=True, default='')

    def __str__(self):
        return f"Transfer {self.id} from {self.origin_account} to {self.destination_account}"
