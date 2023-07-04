from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy
from django.contrib.auth.models import User
from .models import Company

# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse("Найдите работу или работника мечты")

def contacts(request):
    return HttpResponse('''
    <div>
        "Phone: +996777123456 <br>
         Email: office@handhunter.kg"
    </div>
''')

def addresses(request):
    return HttpResponse('''
   
    <ul>       
        <ol>
            <li>г Бишкек, пр Чуй, дом 170 <br></li>
            <li>г Бишкек, ул Московская, дом 195</li>
        </ol>
    </ul>
''')


def vacancy_list(request):
    vacacies = Vacancy.objects.all()
    context = {"vacancies": vacacies}
    return render(request, 'vacancies.html', context)

def company_list(request):
    companys = Company.objects.all()
    context = {"companys": companys}
    return render(request, 'companys.html', context)

def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)  # 1
    candidates = vacancy_object.candidate.all()  # list
    context = {
        'vacancy': vacancy_object,
        'candidates_list': candidates,
    }
    return render(request, 'vacancy/vacancy_page.html', context)


def search(request):
    word = request.GET["keyword"]
    vacancy_list = Vacancy.objects.filter(title__contains=word)
    context = {"vacancies": vacancy_list}
    return render(request, 'vacancies.html', context)

def reg_view(request):
    if request.method == "POST":
        user = User(
            username=request.POST["username"]
        )
        user.save()
        user.set_password(request.POST["password"])
        user.save()
        return HttpResponse("Готово")

    return render(
        request,
        "auth/registr.html"
    )

def vacancy_add(request):
    if request.method == "POST":
        new_vacancy = Vacancy(
            title=request.POST["title"],
            salary=int(request.POST["salary"]),
            description=request.POST["description"],
            email=request.POST["email"],
            contacts=request.POST["contacts"],
        )
        new_vacancy.save()
        return redirect(f'/vacancy/{new_vacancy.id}/')
    return render(request, 'vacancy/vacancy_form.html')

def vacancy_edit(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.method == "POST":
        vacancy.title = request.POST["title"]
        vacancy.salary = int(request.POST["salary"])
        vacancy.description = request.POST["description"]
        vacancy.email = request.POST["email"]
        vacancy.contacts = request.POST["contacts"]
        vacancy.save()
        return redirect(f'/vacancy/{vacancy.id}/')
    return render(
        request, 'vacancy/vacancy_edit_form.html',
        {"vacancy": vacancy}
    )
