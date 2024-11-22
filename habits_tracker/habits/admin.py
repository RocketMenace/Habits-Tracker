from django.contrib import admin
from .models import RegularHabit, RelatedHabit

# Register your models here.


@admin.register(RegularHabit)
class RegulaHabitAdmin(admin.ModelAdmin):

    list_display = ["id"]


@admin.register(RelatedHabit)
class RelatedHabitAdmin(admin.ModelAdmin):

    list_display = ["id"]
