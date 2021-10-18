from django.db import models

class CurrentCryptoPrice(models.Model):
    updated_at = models.DateTimeField(auto_now = True)
    current_price = models.FloatField()
    pair_name = models.CharField(max_length=100,primary_key = True, 
                                 help_text="from and to currency pairs which help identity "
                                           "the quotes should be : seprate example BTC:USD ")
