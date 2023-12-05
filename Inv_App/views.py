from django.shortcuts import render
from .forms import YourForm
from Inv_App.utils import send_to_telegram


def home(request):
    return render(request, 'Inv_App/home.html', context={})

def form_view(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            # Process the form data
            data = form.cleaned_data

            # Send data to Telegram
            send_to_telegram(data)

            # Additional logic or redirect
    else:
        form = YourForm()

    return render(request, 'your_template.html', {'form': form})
