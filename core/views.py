from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy
from .forms import VacancyForm
from .forms import VacancyEditForm
from django.contrib.auth.models import User
from .models import Company
from .forms import CompanyForm
from .forms import CompanyEditForm

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
    return render(request, 'company/companys.html', context)

def company_info(request, id):
    company_object = Company.objects.get(id=id)
    return render(
        request, 'company/companys_detail.html',
        {'company': company_object}
    )

def companys_add(request):
    if request.method == "POST":
        new_company = Company(
            name=request.POST["name"],
            founding_date=request.POST["founding_date"],
            address=request.POST["address"],
            number_of_employees=int(request.POST["number_of_employees"]),

        )
        new_company.save()
        return redirect(f'/company/{new_company.id}/')
    return render(request, 'company/companys_form.html')

def company_add_via_django_form(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save
            return redirect(f'/company/{new_company.id}/')
    companys_form = CompanyForm()
    return render(
        request,
        'company/companys_django_form.html',
        {"companys_form": companys_form}
    )

def company_edit(request, id):
    company_object = Company.objects.get(id=id)

    if request.method == "GET":
        form = CompanyEditForm(instance=company_object)
        return render(request, "company/companys_edit.html", {"form": form})

    elif request.method == "POST":
        form = CompanyEditForm(data=request.POST, instance=company_object)
        if form.is_valid():
            obj = form.save()
            return redirect(company_list(), id=obj.id)
        else:
            return HttpResponse("Форма не валидна")

def vacancy_edit_form(request, id):
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



def vacancy_detail(request, id):
    vacancy_object = Vacancy.objects.get(id=id)  # 1
    candidates = vacancy_object.candidate.all()  # list
    context = {
        'vacancy': vacancy_object,
        'candidates_list': candidates,
    }
    return render(request, 'vacancy/vacancy_page.html', context)

def vacancy_edit(request, id):
    vacancy_object = Vacancy.objects.get(id=id)

    if request.method == "GET":
        form = VacancyEditForm(instance=vacancy_object)
        return render(request, "vacancy/vacancy_edit.html", {"form": form})

    elif request.method == "POST":
        form = VacancyEditForm(data=request.POST, instance=vacancy_object)
        if form.is_valid():
            obj = form.save()
            return redirect(vacancy_detail, id=obj.id)
        else:
            return HttpResponse("Форма не валидна")


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

def vacancy_add_via_django_form(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            new_vacancy = form.save()
            return redirect(f'/vacancy/{new_vacancy.id}/')
    vacancy_form = VacancyForm()
    return render(
        request,
        'vacancy/vacancy_django_form.html',
        {"vacancy_form": vacancy_form}
    )

def vacancy_edit_form(request, id):
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
