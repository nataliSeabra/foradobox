from django.shortcuts import render
import requests
from lisboaiMain.core.models import Categories,Article,Social
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def index(request,template_name="index.html"): 

    objArticle = Article.objects.filter(state='p').order_by('-updated')
    
    return render(request,template_name,{'articles':objArticle})


def post(request,slug):

    objPost = Article.objects.filter(slug=slug)

    return render(request,"post.html",{"post":objPost})



def pageArticle(request,id):
    
    objArticle = Article.objects.all().filter(categories_id=id)
        
    return render(request,"artigos.html",{"articles":objArticle})

    
def aboutUs(request,template_name="about.html"):

    return render(request,template_name)


def contact(request,template_name="contato.html"):

    return render(request,template_name)    



def email(request,template_name="index.html"):

    value = request.POST.get('name')
    print(value)

    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
   
    send_mail(subject, message, email_from, recipient_list)

    
    return render(request,template_name)