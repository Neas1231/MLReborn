from django import forms


class AllForms(forms.Form):
    city = forms.CharField(label="Город", max_length=30,empty_value="Москва") #
    district = forms.CharField(label="Район", max_length=30) #
    underground = forms.CharField(label="Метро", max_length=30) #
    rooms_count = forms.IntegerField(label="Количество комнат") #
    year_of_construction = forms.IntegerField(label="Год постройки") #
    floor = forms.IntegerField(label="Этаж") #
    floors_count = forms.IntegerField(label="Всего этажей в доме") #
    total_meters = forms.IntegerField(label="Площадь квартиры") #
