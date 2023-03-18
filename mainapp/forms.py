from django import forms
from .models import Questions, Division, Company
from django.core.exceptions import ValidationError

class QuestionForm(forms.ModelForm):
    class Meta:
        model= Questions
        exclude=['date_time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['division_id'].label = "Выберите ваш дивизион"
        self.fields['company'].label = "Выберите ваше предприятие"
        self.fields['no_name_company'].label = 'Название предприятия'
        self.fields['question'].label = "Задайте ваш вопрос генеральному директору Госкорпорации 'Росатом' А.Е. Лихачеву"
        self.fields['email'].label = "Если вы хотите лично получить ответ на ваш вопрос, оставьте электронную почту, на которую необходимо направить ответ."
        self.fields['no_name_company'].required=True
        self.fields['email'].required=False


