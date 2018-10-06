from django.shortcuts import render, get_object_or_404
from . models import Product
from django.http import Http404
# Create your views here.
def product_list_view_page(request):
	queryset = Product.objects.all()
	context = {
	'object_list': queryset
	}
	return render(request, 'list_view.html', context)
def featured_list_view(request):
	queryset = Product.objects.featured()
	
	context={
	'object_list':queryset
	}
	return render(request, 'featured/featured_list.html', context)
def featured_detail_view(request, pk=None):
	instance = Product.objects.get( featured=True, pk=pk)
	
	context = {
	'object':instance
	}
	return render(request, 'featured/featured_detail.html', context)
	

def detail_view(request, pk=None):

	#instance = get_object_or_404(Product, pk=pk)
	# try:
	# 	instance=Product.objects.get(id=pk)
	# except Product.DoesNotExist:
	# 	print("No such Product!")
	# 	raise Http404("No such product!")
	# except:
	# 	print("huh?")
	instance = Product.objects.get_by_id(pk)
	if instance is None:
		raise Http404("No such product!!")
	print(instance)
	qs = Product.objects.filter(id=pk)

	if qs.exists() and qs.count()==1:
		instance = qs.first()
	else:
		raise Http404("Product not  found!")
	context = {
	'object':instance
	}

	
	
	   
	return render(request,'detail_view.html', context)

