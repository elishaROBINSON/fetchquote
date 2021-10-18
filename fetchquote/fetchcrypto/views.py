from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from fetchcrypto.models import CurrentCryptoPrice
from .serializers import CryptoSerializer
from requests import request

class FetchQuoteApiView(APIView):
    # 1. get data from DB
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        price = CurrentCryptoPrice.objects.filter(pair_name = "BTC:USD")
        serializer = CryptoSerializer(price, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        pair = request.data.get("pair_name")
        current_price = Data().fetch_data("alphavantage", pair)
        data = {
            'current_price': current_price, 
            'pair_name': pair
        }
        serializer = CryptoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Data(object):
    def __init__(self) -> None:
        super().__init__()
        import environ
        env = environ.Env()
        environ.Env.read_env("/code/fetchquote/fetchquote/.env")
        self.alphavantage_api_key = env("secrect_key_api")
    
    def fetch_data(self, source, pair):
        if source=="alphavantage":
            from_c, to_c = pair.split(":")
            response = request(url="https://www.alphavantage.co/query",
            params={
                "from_currency": from_c,
                "to_currency": to_c,
                "function": "CURRENCY_EXCHANGE_RATE",
                "apikey": self.alphavantage_api_key
            },
            method="GET").json()
            print(response)
            response=response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
            return float(response)
