from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home(request):
    form_success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f'Portfolio Contact from {name}',
                message=f'From: {name} <{email}>\n\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['satyarajsinhj72@gmail.com'],
                fail_silently=False,
            )
            return redirect('/?sent=1#contact')
    else:
        form = ContactForm()

    form_success = request.GET.get('sent') == '1'

    return render(request, 'portfolio/home.html', {
        'form': form,
        'form_success': form_success,
    })