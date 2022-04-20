from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from poker_app.web.forms import CreateTableForm
from poker_app.web.models import Table


class HomeView(views.TemplateView):
    template_name = 'home_page_no_profile.html'
    # template_name = 'index.html'
    # template_name = 'base.html'


class CreateTableView(views.CreateView):
    template_name = 'create-table.html'
    form_class = CreateTableForm
    success_url = reverse_lazy('dashboard')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs


#
def get_all_tables(request):
    tables = Table.objects.all()

    if not tables:
        return redirect('create table page')

    context = {
        'tables': tables,
    }

    return render(request, 'all_tables.html', context)

# class AllTablesView(views.ListView):
#
