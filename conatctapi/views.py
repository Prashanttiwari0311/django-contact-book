from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def add_contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email']
        )
        return redirect('contact_list')

    return render(request, 'contact_form.html')


def update_contact(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST['email']
        contact.save()

        return redirect('contact_list')

    return render(request, 'contact_form.html', {'contact': contact})


def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(request, 'delete_contact.html', {'contact': contact})