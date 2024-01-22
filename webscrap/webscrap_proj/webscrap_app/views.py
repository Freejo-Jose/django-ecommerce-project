import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Links
# Create your views here.
def home(request):
    Links.objects.all().delete()
    if request.method=='POST':
        url=request.POST.get('link')
        html=requests.get(url)
        bs=BeautifulSoup(html.text,'html.parser')
        for l in bs.find_all('a'):
            address=l.get('href')
            string=l.string
            Links.objects.create(string=string,address=address)
    alldata=Links.objects.all()
    return render(request,'home.html',{'alldata':alldata})