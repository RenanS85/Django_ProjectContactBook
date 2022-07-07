import imp
import django
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        show = True
    )
    paginator = Paginator(contacts,3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/index.html', {
        'contacts': contacts})

    
def see_contact(request, contact_id):
    contact = get_object_or_404(Contact, id = contact_id)

    if not Contact.show:
        raise Http404()
    
    return render(request, 'contacts/see_contact.html', {
        'contact': contact
    })

def search(request):
    term = request.GET.get('term')
    if term == None or not term:
        messages.add_message(request, messages.ERROR, 'ERROR - this field appears to be blank')
        return redirect('index')
    else: 
        messages.add_message(request, messages.SUCCESS, 'Contact found')

    char_fields = Concat('name', Value(' '), 'last_name')
    names_phone = Concat('name', Value(' '), 'last_name', Value(' '), 'phone')
    contacts = Contact.objects.annotate( full_name = char_fields, 
    FullnameWithPhone = names_phone ).filter(
        Q(full_name__icontains = term) | Q(phone__icontains = term) |
         Q(FullnameWithPhone__icontains = term)
    )
    paginator = Paginator(contacts,3)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/search.html', {
        'contacts': contacts})
