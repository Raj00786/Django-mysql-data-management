from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	form = PostForm(request.POST or None,request.FILES or None)
	context = {
		"name":"Not logged In",
		"form":form,
	}
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	return render(request,"blogs/form.html",context)


def post_home(request):
	form = PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	queryset_list = Post.objects.all().order_by('-timestamp')

	paginator = Paginator(queryset_list,4) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    queryset = paginator.page(1)
	except EmptyPage:
	    queryset = paginator.page(paginator.num_pages)

	if request.user.is_authenticated():
		context = {
			"name":"Raj Kumar Meena",
			"queryset":queryset
		}
	else:
		context = {
			"name":"Not logged In",
			"form":form,
			"queryset":queryset
		}
	return render(request,"blogs/index.html",context)

def post_update(request,slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	instance= get_object_or_404(Post,slug=slug)
	
	form = PostForm(request.POST or None,request.FILES or None,instance=instance)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully Updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title":"",
		"instance":instance,
		"form":form
	}

	return render(request,"blogs/form.html",context)	

def post_delete(request,slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance= get_object_or_404(Post,slug=slug)
	instance.delete()
	messages.success(request,"Deleted")
	return redirect("home")

def details(request,slug=None):
	instance = get_object_or_404(Post,slug=slug)
	context = {
		"name":"Not logged In",
		"instance":instance
	}
	return render(request,"blogs/detail.html",context)
