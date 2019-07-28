from django.shortcuts import render, redirect, HttpResponse
from .models import Portoflio
# Create your views here.
def portfolio(request):
    portfolios = Portoflio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})


