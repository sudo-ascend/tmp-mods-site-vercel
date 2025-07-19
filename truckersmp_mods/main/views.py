from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError, HttpResponseNotFound

from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from sqlparse.engine.grouping import align_comments
from django.utils.translation import gettext as _

from main.models import Comment, New, Mod


# Create your views here.
def main(request):
    name = request.GET.get('name')
    comment = request.GET.get('comment')
    page_number = request.GET.get('page')
    if not page_number:
        page_number = "1"
    if name != None and comment != None:
        Comment.objects.create(name=name, content=comment)


    comments = Comment.objects.order_by("-time_create").filter(is_published=1)
    paginator = Paginator(comments, 3)
    comments = paginator.get_page(page_number)

    context = {
        'page_obj': comments,
        'active_page': int(page_number),
    }
    return render(request, "main/main.html", context=context)

def all_mods(request):
    sort_by = request.GET.get('sort_by', 'popularity')
    category = request.GET.get('category', '')
    search_query = request.GET.get('search', '')
    page_number = request.GET.get('page')
    if not page_number:
        page_number = "1"
    mods = Mod.objects.filter(is_published=1)

    # Применяем фильтры
    if search_query:
        mods = mods.filter(title__icontains=search_query) | mods.filter(content__icontains=search_query)

    if category:
        mods = mods.filter(category=category)

    # Применяем сортировку
    if sort_by == 'popularity':
        mods = mods.order_by('-views_count')
    elif sort_by == 'date':
        mods = mods.order_by('-time_create')

    paginator = Paginator(mods, 5)
    mods = paginator.get_page(page_number)

    context = {
        'page_obj': mods,
        'active_page': int(page_number),
        'selected_sort': sort_by,
        'selected_category': category,
        'search_query': search_query,
    }
    return render(request, 'main/all_mods.html', context)


def all_news(request):
    sort_by = request.GET.get('sort_by', 'popularity')
    category = request.GET.get('category', '')
    search_query = request.GET.get('search', '')
    page_number = request.GET.get('page')
    if not page_number:
        page_number = "1"
    news = New.objects.filter(is_published=1)
    # Применяем фильтры
    if search_query:
        news = news.filter(title__icontains=search_query) | news.filter(content__icontains=search_query)

    if category:
        news = news.filter(category=category)

    # Применяем сортировку
    if sort_by == 'popularity':
        news = news.order_by('-views_count')
    elif sort_by == 'date':
        news = news.order_by('-time_create')

    paginator = Paginator(news, 5)
    news = paginator.get_page(page_number)

    context = {
        'page_obj': news,
        'active_page': int(page_number),
        'selected_sort': sort_by,
        'selected_category': category,
        'search_query': search_query,
    }
    return render(request, "main/all_news.html", context)

def about(request):
    return render(request, "main/about.html")

def support(request):
    return render(request, "main/support.html")

def page_not_found(request, exception):
    return render(request, 'main/exceptions/404.html', status=404)

def permission_denied(request, exception):
    return render(request, 'main/exceptions/403.html', status=403)

def bad_request(request, exception):
    return render(request, 'main/exceptions/500.html', status=400)

def server_error(request):
    return render(request, 'main/exceptions/500.html', status=500)

