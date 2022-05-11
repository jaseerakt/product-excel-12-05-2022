# from datetime import time
import time

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
# from . migrate import *
import pandas as pd
import requests
from .models import Customer

# Create your views here.
a=''
def home(request):
    return render(request,'index.html')
def upload_file(request):
    global a
    file = request.FILES['filefield']
    print(file)
    df = pd.read_excel(file, engine='openpyxl')
    a = df
    return render(request,'dropdown.html',{'allcolumns':list(df.columns)})

def select(request):
    url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/customers"
    company = request.POST['select']
    first_name = request.POST['select1']
    last_name = request.POST['select2']
    phone = request.POST['select3']
    email = request.POST['select4']
    notes = request.POST['select5']
    address1 = request.POST['select6']
    address2= request.POST['select7']
    address_type= request.POST['select8']
    address_city= request.POST['select9']
    address_company= request.POST['select10']
    country_code= request.POST['select11']
    address_fname= request.POST['select12']
    address_lname= request.POST['select13']
    address_phone= request.POST['select14']
    postal_code= request.POST['select15']
    state_or_province= request.POST['select16']

    for index,row in a.iterrows():
        payload =[{
            "company": row[company],
            "first_name": row[first_name],
            "last_name": row[last_name],
            "phone": str(row[phone]),
            "email": row[email],
            "notes": row[notes],
            "addresses":[
                {
                    "address_type": row[address_type],
                    "first_name": row[address_fname],
                    "city": row[address_city],
                    "country_code": row[country_code],
                    "last_name": row[address_lname],
                    "company": row[address_company],
                    "phone": str(row[address_phone]),
                    "address1": row[address1],
                    "address2": row[address2],
                    "postal_code": str(row[postal_code]),
                    "state_or_province": row[state_or_province],
               }]
             }]
        print(payload)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
    return home(request)

def product(request):
        return render(request, 'product.html')

def upload_product(request):
    fil = request.FILES['filefield1']
    print(fil)
    ef = pd.read_excel(fil, engine='openpyxl')
    url = "https://api.bigcommerce.com/stores/b5ajmj9rbq/v3/catalog/products"
    for index, row in ef.iterrows():
        payload = [{
            # "company": row"company",
            "product_name": row["name"],
            "product_type": row['type'],
            # "sku": row["sku"],
            # "description": row["description"],
            "weight": str(row["weight"]),
            # "width": row["width"],
            # "depth": row["depth"],
            # "height": row["height"],
            "default_ price": str(row["price"]),
            # "cost_price": row["cost_price"],
            # "retail_price": row["retail_price"],
            # "sale_price": row["sale_price"],
            # "map_price": row["map_price"],
            # "tax_class_id": row["tax_class_id"],
        }]
        print(payload)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Auth-Token": "redptv84kmlgfed97l7jroa0mdknfgc"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        return product(request)