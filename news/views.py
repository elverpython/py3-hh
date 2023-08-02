from django.shortcuts import render, HttpResponse, redirect
from .models import ArticleNew
from .forms import ArticleNewForm

def news_list(request, id):
    resume_object = ArticleNew.objects.get(id=id)
    return render(
        request, 'news/news.html',
        {'news': resume_object}
    )


def news_add(request):
    if request.method == "POST":
        form = ArticleNewForm(request.POST)
        if form.is_valid():
            new_news = form.save()
            return redirect(f'/news/{new_news.id}/')
    news_form = ArticleNewForm()
    return render(
        request,
        'news/news_django_form.html',
        {"news_form": news_form}
    )

