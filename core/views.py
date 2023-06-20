from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("hi")

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