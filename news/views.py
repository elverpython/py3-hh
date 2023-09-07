from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import ArticleNew
from .forms import ArticleNewForm, ArticleEditForm

def news_list(request):
    news_object = ArticleNew.objects.all()
    return render(
        request, 'news/news.html',
        {'news': news_object}
    )

def news_info(request, id):
    news_info_object = ArticleNew.objects.get(id=id)
    return render(request, 'news/news_info.html', {'news_info': news_info_object})

def news_add(request):
    if request.method == "POST":
        form = ArticleNewForm(request.POST)
        if form.is_valid():
            new_news = form.save()
            return redirect(f'/news-info/{new_news.id}/')
    news_form = ArticleNewForm()
    return render(
        request,
        'news/news_form.html',
        {"news_form": news_form}
    )

def news_edit(request, id):
    news_object = ArticleNew.objects.get(id=id)

    if request.method == "GET":
        form = ArticleEditForm(instance=news_object)
        return render(request, "news/news_edit.html", {"form": form})

    elif request.method == "POST":
        form = ArticleEditForm(data=request.POST, instance=news_object)
        if form.is_valid():
            obj = form.save()
            return redirect(news_info, id=obj.id)
        else:
            return HttpResponse("Форма не валидна")

# def news_detail(request, id):
#     new = ArticleNew.objects.get(id=id)
#     new.views_count += 1
#     new.save()
#     return render(request, 'news/news_info.html', {'new': new})

class ArticleNewDetail(View):
    def get(self, request, *args, **kwargs):
        new = ArticleNew.objects.get(id=kwargs['id'])
        new.views_count += 1
        new.save()
        return render(request, 'news/news_info.html', {'new': new})