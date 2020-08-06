from django.shortcuts import render,HttpResponse
from Blog.models import Homestay,Blog,Category
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    
    return render(request,'index.html')

def homestay(request):
    
    homestay=Homestay.objects.all
    context={'homestay':homestay}
    return render(request,'homestay.html',context)

def blog(request):
    allpost=Blog.objects.all()
    
    category=Category.objects.all()
    
    
    paginator=Paginator(allpost, 1)
    page=request.GET.get('page')
    allpost=paginator.get_page(page) 
    


    context={'allpost':allpost,'category':category}
    return render(request,'blog.html',context)

def contact(request):
    
    return render(request,'contact.html')


def homestays(request,slug):

    home = Homestay.objects.filter(slug=slug)
    
    return render(request,'homestays.html')
    
    
def blogpost(request,slug):
    post=Blog.objects.filter(slug=slug).first()
    
    post.views=post.views+1
    post.save()
    context={'post':post}
    return render(request,'blogpost.html',context)

