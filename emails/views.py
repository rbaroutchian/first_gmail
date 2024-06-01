from django.shortcuts import render, redirect
from django.views import View
from .models import Email, Inbox
from .Form import EmailForm
from django.contrib.auth.mixins import LoginRequiredMixin


class EmailCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = EmailForm()
        return render(request, 'create_email.html', {'form': form})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = request.user
            email.save()
            return redirect('email_list')  # Replace with your desired redirect URL name
        return render(request, 'create_email.html', {'form': form})


class EmailListView(LoginRequiredMixin, View):
    def get(self, request):
        emails = Email.objects.filter(sender=request.user) | Email.objects.filter(recipient=request.user)
        return render(request, 'email_list.html', {'emails': emails})


class InboxView(LoginRequiredMixin, View):
    def get(self, request):
        # بازیابی ایمیل‌ها از مدل Inbox
        emails = Inbox.objects.filter(user=request.user)

        # آماده‌سازی داده‌ها برای ارسال به قالب HTML
        email_data = []
        for email in emails:
            email_data.append({
                'subject': email.subject_objects,
                'body': email.body_objects
            })

        return render(request, 'inbox.html', {'emails': email_data})
