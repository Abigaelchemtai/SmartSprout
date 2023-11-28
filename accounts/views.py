from django.contrib import messages
from django.shortcuts import render, redirect

from academia.forms import CreateUserForm


# Create your views here.
def signupPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was Created for' + user)

            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/Signup.html', context)


def login(request):
    return render(request, 'registration/Login.html')

