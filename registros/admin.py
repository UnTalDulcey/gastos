from django.contrib import admin

# Register your models here.
from registros.models import Gasto


@admin.register(Gasto)
class AdminModel(admin.ModelAdmin):
    pass