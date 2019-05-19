from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from contact.forms import ContactForm

def About(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = f'{0} you got email from:\n\n {1}'.format(sender_name, form.cleaned_data['message'])
            send_mail('New Email', message, sender_email, ['nissanskyline719@gmail.com'])
            messages.success(request, f'Thank you for contacting us!.')
            return redirect('About')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
