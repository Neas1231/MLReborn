#методы, которые будут вызваны при переходе пользователя на какую-либо определенную страницу
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AllForms
from .lemmatize import *
import joblib

def index(request):
      form = AllForms()     #request просто надо
      if request.method == "POST":
        form = AllForms(request.POST)
        if form.is_valid():
          city = form.cleaned_data['city']
          district = form.cleaned_data['district']
          underground = form.cleaned_data['underground']
          rooms_count = form.cleaned_data['rooms_count']
          year_of_construction = form.cleaned_data['year_of_construction']
          floor = form.cleaned_data['floor']
          floors_count = form.cleaned_data['floors_count']
          total_meters = form.cleaned_data['total_meters']
          city = lemmatize(city)
          district = lemmatize(district)
          underground = lemmatize(underground)
          trans = ['апрелевка', 'балашиха', 'бронницы', 'чехов', 'дедовск', 'дмитров', 'долгопрудный', 'домодедово', 'дубна',
           'дзержинский',
           'электросталь', 'фрязино', 'истра', 'ивантеевка', 'кашира', 'химки', 'хотьково', 'клин', 'коломна',
           'королев', 'котельники',
           'красногорск', 'ликино дулево', 'лобня', 'лосино петровский', 'луткарино', 'люберцы', 'мытищи',
           'наро фоминск', 'ногинск',
           'одинцово', 'подольск', 'пушкино', 'раменское', 'реутов', 'рошаль', 'руза', 'сергиев посад', 'серпухино',
           'щелково', 'солнечногорск',
           'старая купавна', 'ступино', 'талдом', 'видное', 'волокамск', 'воскресенск', 'москва', 'яхрома', 'егорьевск',
           'жуковский', 'звенигород']
          le_c = joblib.load('D:\Загрузки\intensiv23\metl\main\static\ML\label_encoder_city.joblib')
          le_d = joblib.load('D:\Загрузки\intensiv23\metl\main\static\ML\label_encoder_district.joblib')
          le_u = joblib.load('D:\Загрузки\intensiv23\metl\main\static\ML\label_encoder_underground.joblib')
          dic = dict(zip(trans, list(le_c.classes_)))

          if city in dic.keys():
            city = dic[city]
          else:
            city ='www'
          city = le_c.transform([city])[0]

          if district in le_d.classes_:
            district = le_d.transform([district])[0]
          else:
            district = 'unk'
            district = le_d.transform([district])[0]

          if underground in le_u.classes_:
            underground = le_u.transform([underground])[0]
          else:
            underground = 'unk'
            underground = le_u.transform([underground])[0]

          to_pred = [city,district,underground,floor,floors_count,rooms_count,total_meters,year_of_construction]
          model = joblib.load('D:\Загрузки\intensiv23\metl\main\static\ML\price(only total_meters).joblib')
          print('Результат', abs(model.predict(to_pred))/total_meters)
          return render(request, 'main/shapka.html',{"form": form})

    # if a GET (or any other method) we'll create a blank form
        else:
          form = AllForms()
      return render(request, 'main/osnova.html',{"form": form})      #return возвращаем этот обьект на основе этого класса


                            #render нужен для того, чтобы выбрать конкретный html шаблон, который нужно показывать
def user_start(request):
  return render(request, 'main/osnova.html')
def user_end(request):
  return render(request, 'main/osnova.html')

