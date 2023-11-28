from django.shortcuts import render,redirect
from .forms import OrderForm, ContactForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact, Orders

# Create your views here.

def index(request):
    return render(request, 'index.html')


def navigation(request):
    return render(request, 'navigation.html')


@login_required()
def services(request):
    return render(request, 'services.html')


@login_required()
def explore(request):
    return render(request, 'explore.html')



@login_required()
def ContactUs(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            new_contact = contact_form.save()
            messages.success(request, f'New Contact Created')
            return redirect('contact')
        else:
            messages.error(request, f'Contact Form Is Not Valid! Please Check The Entered Data!!')
    else:
        contact_form = ContactForm()
        all_contact = Contact.objects.all()

        return render(request, 'contact.html', {'contact_form': contact_form, 'all_contact':all_contact })


@login_required()
def CreateOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        messages.success(request, 'Message was Received. Well Contact you soon')

    context = {'form':form}
    return render(request, 'orders.html', context)

@login_required()
def UpdateOrder(request):
    form = OrderForm()
    context = {'form': form}
    return render(request, 'orders.html', context)


