from django.shortcuts import render

from .forms import PayForm


def pay(request):
    form = PayForm()
    context = {'form': form}
    return render(request, 'pay/pay_form.html', context)
