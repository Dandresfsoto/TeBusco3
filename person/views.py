from django.views.generic import TemplateView
from person.models import Person

class HomeView(TemplateView):
    template_name = 'prueba/home.html'

    def get_context_data(self, *args, **kwargs):
        persons = Person.objects.all()
        return {'persons':persons}