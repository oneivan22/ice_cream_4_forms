from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContestForm
from .models import Contest


def proposal_create(request):
    form = ContestForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    contests = Contest.objects.all().order_by('id')
    context = {'contests': contests}
    return render(request, 'contest/list.html', context)


def proposal_edit(request, pk):
    instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'contest/form.html', context)


def proposal_delete(request, pk):
    instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        instance.delete()
        return redirect('contest:list')
    return render(request, 'contest/form.html', context)


def accepted(request):
    return render(request, 'contest/proposal_accepted.html')