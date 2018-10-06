from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm,LoginForm, RegisterForm
from django.contrib.auth import authenticate,login, get_user_model
def home_page(request):
	context={
	"tittle":"Welcome to the home page",
	"content":"Welcome to our very first ever homepage",
	"premium":"yoyoyoyo"
	}
	return render(request,'home_page.html',context)
def  about_page(request):
	context={
	"tittle":"Welcome to the about page",
	"content":"Welcome to our very first ever aboutpage"
	}
	return render(request,'home_page.html',context)
def login_page(request):
	form = LoginForm(request.POST or None)
	print(request.user.is_authenticated())
	context={
	'form':form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request,user)
			redirect('login/')
			print(request.user.is_authenticated())
		else:
			print("error")

	return render(request,'auth/login.html', context)
user = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
	'form':form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = user.objects.create_user(username,email,password)
		print(new_user)
	return render(request,'auth/register.html', context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context={
	"tittle":"Welcome to the contact page",
	"content":"Welcome to our very first ever contactpage",
	"form":contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	# if request.method =='POST':
	# 	print(request.POST)
	# 	print(request.POST.get('fullname'))
	# 	print(request.POST.get('email	# 	print(request.POST.get('content'))

	return render(request,'contact/view.html',context)
def home_page_old(request):
	html = """
	
	<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    
    <title>Hello, world!</title>
    
  </head>
  <body>
  <div class ='text-center'>
    <h1>Hello, world!</h1>
   </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>
	"""
	return HttpResponse(html)