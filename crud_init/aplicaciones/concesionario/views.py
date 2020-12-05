from django.shortcuts import render, redirect
from .models import User, Car
from .forms import Logingform, CarForm


# Create your views here.
# We have to import our models

def loging(request):
    # if request method is GET load template with form

    ctx = {
        'loging_form': Logingform()
    }

    if request.method == 'POST':
        # if method is post charge
        form_post_values = [request.POST['username'], request.POST['email'], request.POST['password']]
        # print(form_post_values)
        all_users = User.objects.all()
        # loop the query separating by lists
        for field in all_users:
            if str(field).split(" ")[1] == form_post_values[0] and \
                    str(field).split(" ")[2] == form_post_values[1]:
                print("El usuario existe")
                return redirect('crud')
        # if usser dont exist add error to context and redirect with error
        ctx['error'] = 'si'
    return render(request, 'index.html', ctx)


def register(request):
    if request.method == 'GET':
        ctx = {
            'register_form': Logingform()
        }
        return render(request, 'register.html', ctx)
    if request.method == 'POST':
        form = Logingform(request.POST)
        ctx = {
            'register_form': form
        }

        form_post_values = [request.POST['username'], request.POST['email'], request.POST['password']]
        # print(form_post_values)
        all_users = User.objects.all()

        # loop the query separating by lists
        for field in all_users:
            print(str(field).split(" ")[1])
            print(form_post_values[0])
            if str(field).split(" ")[1] == form_post_values[0] or str(field).split(" ")[2] == form_post_values[1]:
                print(form_post_values)
                ctx['error'] = 'si'
                return render(request, 'register.html', ctx)

        if form.is_valid():
            form.save()
            return redirect('crud')


def crud(request):
    cars = Car.objects.all()
    for car in cars:
        print(car)
    ctx = {
        'cars': cars
    }
    return render(request, 'crud.html', ctx)


def add_car(request):
    global ctx
    if request.method == 'GET':
        ctx = {
            'cars_form': CarForm()
        }
    if request.method == 'POST':
        form = CarForm(request.POST)
        ctx = {
            'cars_form': form
        }
        if form.is_valid():
            form.save()
            print("Guardado")
            return redirect('crud')

    return render(request, 'form_car.html', ctx)


def edit_car(request, id):
    global ctx
    car = Car.objects.get(id=id)
    print(car)
    if request.method == 'GET':
        form = CarForm(instance=car)
        ctx = {
            'cars_form': form
        }
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        ctx = {
            'cars_form': form
        }
        print("yes")
        if form.is_valid():
            print("is_valid")
            form.save()
            return redirect('crud')

    return render(request, 'form_car.html', ctx)


def delete_car(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    cars = Car.objects.all()
    ctx = {'cars': cars, 'delete': True}
    return render(request, 'crud.html', ctx)


"""
add_car, edit_car, delete_car
"""
