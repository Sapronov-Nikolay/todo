from django.db import models
from django.utils import timezone 
# После импорта модуля timezone мы можем использовать параметр timezone.now в качестве аргумента 
# по умолчанию для date_created. 
# Теперь при создании новой записи не придётся вручную указывать время и дату. 
# Это пригодится нам позже

class Delo(models.Model): # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    title = models.CharField(max_length=100)
    content = models. TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self): # С помощью функции меняем то, как будет представлена запись в модели.
        return self.title # Указываем, что она будет идентифицироваться с помощью своего заголовка.
    
    class Meta:
        verbose_name_plural = "Dels" # Указываем правильное написание для множественного числа слова Delo.