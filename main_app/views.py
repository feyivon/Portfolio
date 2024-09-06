from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def home_page(request):
    return render(request, 'main/index-2.html')


def about_page(request):
    return render(request, 'main/index.html')



def portfolio_page(request):
    return render(request, 'main/portfolio.html')


# def blog_page(request):
#     return render(request, 'main/blog-topbar.html')

# def service_page(request):
#     return render(request, 'main/service.html')


def contact_page(request):
    return render(request, 'main/contact.html')

# def read_more(request):
#     if request.method=='POST':
#         form=Descriptionform(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('services')
#         print(form.errors)
#     else:
#         form=Descriptionform()
#     context ={
#         'form': form
#     }
#     return render(request, 'main/read_more.html', context)


# def cv_page(request)
