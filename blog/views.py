import random
import json
from django.utils.text import Truncator
from el_pagination.decorators import page_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models.aggregates import Count
from random import randint

from .models import Post, SiteImage, SiteLink, Comment, Paragraph



def index(request):
	#page_template = 'blog/index_page.html'
	template = 'blog/index.html'
	latest_post_list = Post.objects.all()
	context = {'latest_post_list': latest_post_list}
	
	return render(request, template, context)
	#return HttpResponse("Testing..")

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/detail.html', {'post': post})

def add_comment(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	p = Comment()
	p.comment_author = request.POST.get('i1')
	p.comment_text = request.POST.get('i2')
	p.post_id = post.id
	p.save()
	response_data = {'author': p.comment_author, 'text': p.comment_text}
	return HttpResponse(json.dumps(response_data), content_type='application/json')
	#return HttpResponseRedirect(reverse('blog:detail', args=(post.id, )))

def add_like(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.votes += 1
	post.save()
	#return HttpResponse(post.votes)
	response_data = {'likes': post.votes}
	
	return HttpResponse(json.dumps(response_data), content_type='application/json')
	#return HttpResponseRedirect(reverse('blog:detail', args=(post.id, )))

def other_pages(request):
	#page_template = 'blog/index_page.html'
	template = 'blog/others.html'
	latest_post_list = Post.objects.filter(category='general')
	context = {'latest_post_list': latest_post_list}
	return render(request, template, context)
	#return HttpResponse("Testing..")

def movies(request):
	#page_template = 'blog/index_page.html'
	template = 'blog/movies.html'
	latest_post_list = Post.objects.filter(category='movies')
	context = {'latest_post_list': latest_post_list}
	return render(request, template, context)
	#return HttpResponse("Testing..")

def videos(request):
	#page_template = 'blog/index_page.html'
	template = 'blog/videos.html'
	latest_post_list = Post.objects.filter(category='videos')
	context = {'latest_post_list': latest_post_list}
	return render(request, template, context)
	#return HttpResponse("Testing..")

def conversations(request):
	#page_template = 'blog/index_page.html'
	template = 'blog/conversations.html'
	latest_post_list = Post.objects.filter(category='conversations')
	context = {'latest_post_list': latest_post_list}
	return render(request, template, context)
	#return HttpResponse("Testing..")

def doodles(request):
	#page_template = 'blog/index_page.html'
	template = 'blog/doodles.html'
	latest_post_list = Post.objects.filter(category='doodles')
	context = {'latest_post_list': latest_post_list}
	return render(request, template, context)
	#return HttpResponse("Testing..")



def shuffle(request):
	template = 'blog/shuffle.html'
	latest_post_list = Post.objects.order_by('?')[:25]
	context = {'latest_post_list': latest_post_list}
	return render(request, template, context)

def search_site(request):
	search_word = request.GET.get('s1')
	if(search_word == ""):
		raise Http404
	search_word = search_word.lower()
	template = 'blog/search.html'
	latest_post_list = []
	for p in Post.objects.all():
		if(p.post_title.lower().find(search_word) != -1):
			latest_post_list.append(p)
		else:
			for ps in p.paragraph_set.all():
				if((ps.paragraph_text.lower().find(search_word) != -1)):
					latest_post_list.append(p)
					break


	context = {'latest_post_list': latest_post_list}
	
	return render(request, template, context)	


