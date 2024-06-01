from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from pyexpat.errors import messages

from .Form import SignUpForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'ثبت نام با موفقیت انجام شد.')
            return redirect('signin')  # Replace 'home' with the name of your desired URL pattern
        else:
            messages.error(request, 'لطفاً خطاهای زیر را اصلاح کنید.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Assuming the username field is email
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a different page after signin
                return redirect('create-email')  # Replace 'home' with the name of your desired URL pattern
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})
