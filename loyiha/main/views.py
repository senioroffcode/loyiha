from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


@api_view(['GET'])
def get_home(request):
       home = Home.objects.all()
       serialized_data = HomeSerializer()
       return Response(serialized_data.data)

@api_view(['PUT'])
def create_order(request):
       title = request.POST.get('title')
       text = request.POST.get('text')
       name = request.POST.get('name')
       phone = request.POST.get('phone')
       product = Product.objects.create(
              title=title,
              text=text,
              name=name,
              phone=phone,
       )
       product.save()
       hello = OrderSerializer(product)
       return Response(hello)

@api_view(['GET'])
def get_ads(request):
       ads = Ads.objects.all()
       serialized_data = AdsSerializer()
       return Response(serialized_data.data)


@api_view(['GET'])
def get_product(request):
       product = Product.objects.all()
       serialized_data = ProductSerializers()
       return Response(serialized_data.data)


@api_view(['GET'])
def get_prod(request):
       prod = Prod.objects.all()
       serialized_data = ProdSerializers()
       return Response(serialized_data.data)

@api_view(['GET'])
def get_company(request):
       company = Company.objects.all()
       serialized_data = CompanySerializers()
       return Response(serialized_data.data)

@api_view(['GET'])
def get_question(request):
       question = Question.objects.all()
       serialized_data = QuestionSerializers()
       return Response(serialized_data.data)

@api_view(['GET'])
def get_method(request):
       method = Method.objects.all()
       serialized_data = MethodSerializers()
       return Response(serialized_data.data)

@api_view(['GET'])
def get_fact(request):
       fact = Fact.objects.all()
       serialized_data = FactSerializers()
       return Response(serialized_data.data)