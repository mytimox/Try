from django.contrib import admin
from .models import PIB
# Register your models here.


class PIBAdmin(admin.ModelAdmin):

   # list_display = ["first_name", "last_name", "email", "id"]
    # Виводить в адмінці всі поля з моделі
    list_display = [field.name for field in PIB._meta.fields]
   # виключає поле years
    exclude = ["last_name"]
    # створює фільтр по імені
    list_filter = ["first_name"]
    #Добавляє поле пошуку
    search_fields = ['email']

    class Meta:
        model=PIB

admin.site.register(PIB, PIBAdmin)