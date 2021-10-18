from celery import task 
from fetchcrypto.serializers import CryptoSerializer
from fetchcrypto.views import Data

@task(name='scheduled_update_pair') 
def update_BTC_USD():
     pair = "BTC:USD"
     current_price = Data().fetch_data("alphavantage", pair)
     print(current_price)
     data = {
            'current_price': current_price, 
            'pair_name': pair
        }
     serializer = CryptoSerializer(data=data)
     serializer.save()
     print("data saved")