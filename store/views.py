from django.shortcuts import render
from .models import Product, ProductImage, Category, SubCategory, Shop
from blog.models import BlogPost
from django.http import HttpResponse
from django.core.mail import EmailMessage
# Create your views here.
def home(request):
	products = Product.objects.all()
	templates = 'index.html'
	blog = BlogPost.objects.all()
	context = {'products':products, 'blog':blog}
	return render(request, templates, context)


def about(request):
	return render(request,'about.html')

def shop(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	shop = Shop.objects.all()
	templates = "shop.html"
	context = {'products':products, 'categories': categories,'shop':shop}
	return render(request, templates, context)
		
def form(request):
	if request.method=="GET":
		return render(request, 'form.html')

	elif request.method=='POST':
		Name= request.POST['Name']
		Email = request.POST['Email']
		Quantity = int(request.POST['Quantity'])
		subject = "Reply for Quotation Request"
		body = "Contents of Body"
		from_email = "electrostorenepal@gmail.com"
		to = [Email]
		

		msg = EmailMessage(subject, body, from_email, to,)
		if Quantity<=30:
			msg.attach_file('static/img/gallery.jpg')
		else:
			msg.attach_file('static/img/logo.png')

		if msg.send(fail_silently=False):
			return HttpResponse("Success")
		else:
			return HttpResponse("failed")









	
def contact(request):
	return render(request,'contact.html')

def services(request):
	return render(request,'services.html')


def details(request, id):
	categories = Category.objects.all()
	
	return render(request, 'shop-item.html', {'products':Product.objects.get(pk=id), 'categories':	categories })

def subcategory(request, id):
	
	categories = Category.objects.all()
	subcat = SubCategory.objects.get(id = id)

	return render(request, 'shop.html', {'products':subcat.reference.all() , 'categories':	categories })