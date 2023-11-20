from django.contrib import admin
from .models import Task

class TasksAdmin(admin.ModelAdmin):
    #list_display = ('title', 'author', 'price')
    list_display = [  # генератор-выражение, формирующее список полей нашеё таблицы для отображения в админке
        field.name for field in Task._meta.fields if field.name != "id"]

#>>> my_list_1 = [i for i in range(25)]
#>>> print(my_list_1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


admin.site.register(Task, TasksAdmin)
