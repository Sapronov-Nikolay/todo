from mainpage import models
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = models.Task
        fields = [ #генератор-выражениеб формирующее список полей таблицы для отображения в админке
            field.name for field in models.Task._meta.fields if field.name != "id"]