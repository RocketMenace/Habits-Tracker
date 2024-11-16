from django.contrib import admin
from .models import RegularHabit, RelatedHabit

# Register your models here.


@admin.register(RegularHabit)
class RegulaHabitAdmin(admin.ModelAdmin):

    pass


@admin.register(RelatedHabit)
class RelatedHabitAdmin(admin.ModelAdmin):

    pass
