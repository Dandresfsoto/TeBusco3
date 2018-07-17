from django.contrib import admin
from person.models import Person, PersonImage


class PersonImageInLine(admin.TabularInline):
    model = PersonImage


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        PersonImageInLine
    ]


admin.site.register(Person, PersonAdmin)
