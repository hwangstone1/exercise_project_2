from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(reqeust):
    return render(reqeust, 'main/main.html')