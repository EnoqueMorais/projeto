from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def home(request):
    return render (request, 'index.html', {})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user/list.html',{'users':users})

@staff_member_required
@login_required
def user_delete(request, user_id):
    user = User.objects.get(pk=user_id)
    user.delete()
    messages.success(request, 'Usuario apagado com sucesso!!')
    return redirect('/polls/user/')