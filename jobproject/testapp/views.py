from django.shortcuts import render
from django.urls import reverse_lazy
from testapp.models import client
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView

def home_view(request):
    return render(request,'testapp/home.html')

class clientCreate(CreateView):
    model=client
    fields=('cid','cname','cdate','cby')
class clientList(ListView):
    model=client
class clientDetail(DetailView):
    model=client
class clientUpdate(UpdateView):
    model=client
    fields=('cname','cdate','cby')
class clientDelete(DeleteView):
    model=client
    success_url=reverse_lazy('list')
