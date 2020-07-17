from django.shortcuts import render, HttpResponse
from django.http import HttpResponse

html_base = """
    "<h1>MI WEB PERSONAL</h1>
    <u1>
        <li><a href="/">Portada</a</li>
        <li><a href="/about/">Acerca de...</a</li>
        <li><a href="/portfolio/">Portafolio</a</li>
        <li><a href="/contact/">Contacto</a</li>
    </u1>
"""
# Create your views here.



def home(request):
    return render(request, "core/home.html")

def about(request):
     return render(request, "core/about.html")

def contact(request):
     return render(request, "core/contact.html")

