from django.shortcuts import render, redirect
from .models import Lead
from .forms import LeadModelForm

def landing_page(request):
    return render (request,'landing_page.html')

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads/lead_list.html', context)

def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {
        'lead': lead,
    }
    return render(request, 'leads/lead_detail.html', context)


def lead_create(request):
    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')
        else:
            print('error creating form')
    
    context = {
        'form': form
    }
    return render(request,'leads/lead_create.html', context)


def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect(f'/leads/{pk}')
        else:
            print('error creating form')
    
    context = {
        'lead': lead,
        'form': form
    }
    return render(request,'leads/lead_update.html', context)

def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('/leads')
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_delete.html',context)