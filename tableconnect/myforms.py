from django import forms
from .models import *



class FormJuice(forms.Form):
    name = forms.ModelChoiceField(Product.objects.values_list('name', flat=True).distinct(),
                                   required=False, to_field_name='name', empty_label='', label='Название')
    firma = forms.ModelChoiceField(Company.objects.values_list('title', flat=True),
                                   required=False, to_field_name='title', empty_label='', label='Фирма')
    volume = forms.ModelChoiceField(Product.objects.values_list('volume', flat=True).distinct(),
                                   required=False, to_field_name='volume', empty_label='', label='Объём')
    pack = forms.ModelChoiceField(Product.objects.values_list('pack', flat=True).distinct(),
                                   required=False, to_field_name='pack', empty_label='', label='Упаковка')
    recomend = forms.ModelChoiceField(Product.objects.values_list('recomend', flat=True).distinct(),
                                   required=False, to_field_name='recomend', empty_label='', label='Рекоменд')


class FormStudents(forms.Form):
    course = forms.ModelChoiceField(Course.objects.all(), required=False, empty_label='', label='Курс')
    student = forms.ModelChoiceField(Student.objects.all(), required=False, empty_label='', label='Студент')
