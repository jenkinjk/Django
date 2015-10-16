from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate

from contacts.models import contact
from contacts.forms import contactForm, loginForm, searchForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def search(request):
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = searchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            searchTerm= form.cleaned_data['search']
            contact_list = contact.objects.filter(first_name__contains=searchTerm) | contact.objects.filter(last_name__contains=searchTerm) | contact.objects.filter(phone_number__contains=searchTerm) | contact.objects.filter(street_address__contains=searchTerm) | contact.objects.filter(email_address__contains=searchTerm)
            context = {'contacts_list': contact_list}
            return render(request, 'contacts/viewAll.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = searchForm()
    return render(request, 'contacts/search.html', {'form': form})

def newUser(request):
  form = UserCreationForm()
  print("In new User")
  if form.is_valid():
      print("Form is valid")
      user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['password'])
      form = loginForm()
      return render(request, 'contacts/login.html', {'form': form})
  else:
    form = UserCreationForm()
    return render(request, 'contacts/newUser.html', {'form': form})

def logout_view(request):
    logout(request)
    form = loginForm()
    return HttpResponseRedirect('/contacts/login')

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        print("Recieved the login")
        if form.is_valid():
            print("It is valid")
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            print("username is " + form.cleaned_data['username'])
            print("password is "+form.cleaned_data['password'])
            print(user)
            if user is not None:
              print("it is not none")
              if user.is_active:
                print("it is active")
                return HttpResponseRedirect('/contacts/')
            else:
              form = loginForm()
              return render(request, 'contacts/login.html', {'form': form})
    else:
        form = loginForm()

    return render(request, 'contacts/login.html', {'form': form})

def index(request):
    contact_list = contact.objects.order_by('last_name')
    context = {'contacts_list': contact_list}
    return render(request, 'contacts/index.html', context)

def detail(request, contact_id):
    contactObject = get_object_or_404(contact, id = contact_id)
    if request.method == 'POST':
      contactObject.delete()
      return HttpResponseRedirect('/contacts/')
    else:
      return render(request, 'contacts/detail.html', {'contact': contactObject})

def new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = contactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone_number']
            email = form.cleaned_data['email_address']
            address = form.cleaned_data['street_address']
            contactObject = contact(first_name = firstName, last_name = lastName, phone_number = phone, email_address = email, street_address = address)
            contactObject.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/contacts/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = contactForm()

    return render(request, 'contacts/new.html', {'form': form})

def viewAll(request):
    contact_list = contact.objects.order_by('last_name')
    context = {'contacts_list': contact_list}
    return render(request, 'contacts/viewAll.html', context)
