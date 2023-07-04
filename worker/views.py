from django.shortcuts import render,redirect, HttpResponse
from .models import Worker, Resume

# Create your views here.

def worker_list(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    return render(request, 'workers.html', context)

def worker_info(request, id):
    worker_object = Worker.objects.get(id=id)
    context = {"worker": worker_object}
    return render(request, "worker.html", context)


def resume_list(request):
    resume_query = Resume.objects.all()
    return render(
        request, 'resume/resume_list.html',
        {"resumes": resume_query}
    )


def resume_info(request, id):
    resume_object = Resume.objects.get(id=id)
    return render(
        request, 'resume/resume_detail.html',
        {'resume': resume_object}
    )


def my_resume(request):
    resume_query = Resume.objects.filter(worker=request.user.worker)
    # resume_query = request.user.worker.resume.all()
    return render(
        request, 'resume/resume_list.html',
        {"resumes": resume_query}
    )

def add_resume(request):
    template = 'resume/resume_add.html'
    if request.method == "GET":
        # показать форму
        return render(request, template)
    elif request.method == "POST":
        # записать резюме в БД
        new_resume = Resume()
        new_resume.worker = request.user.worker
        new_resume.title = request.POST["form-title"]
        new_resume.text = request.POST["form-text"]
        new_resume.save()
        return HttpResponse("Запись добавлена!")

def resume_edit(request, id):
    resume = Resume.objects.get(id=id)
    if request.method == "POST":
        resume.title = request.POST["title"]
        resume.text = request.POST["text"]
        resume.save()
        return redirect(f'/vacancy/{resume.id}/')
    return render(
        request, 'resume/resume_edit_form.html',
        {"resume": resume}
    )

