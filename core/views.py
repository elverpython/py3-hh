from django.shortcuts import render, HttpResponse
from .models import Vacancy
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

def vacancy(request, id):
    vacancy = Vacancy.objects.get(id=id)
    return render(
        request, 'vacancy/vacancy.html',
        {'vacancy': vacancy}
    )