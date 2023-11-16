from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    #Products.objects.all() returns all products in DB
    #Products.objects.filter() filters out products based on a condition "out of stock or that cost more than $100"
    #Products.objects.get() getting a single product
    #Products.objects.save() inserting a new product or updating an exisitng one
    
    products = Product.objects.all()
    return render(request, "index.html",{"products": products})

def new(request):
    return HttpResponse("New products! Just in today!")