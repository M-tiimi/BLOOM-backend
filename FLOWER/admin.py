from django.contrib import admin

# Register your models here.
from .models import Flower, Answer, Question, Task, User

admin.site.register(Flower)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Task)