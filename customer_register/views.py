from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Home View
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from social_django.models import UserSocialAuth

from customer_register.models import Customer
from django.shortcuts import render , redirect
from .forms import CustomerForm
from .models import Customer
 



# Create your views here.

class SettingsView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user

        try:
            github_login = user.social_auth.get(provider='github')
        except UserSocialAuth.DoesNotExist:
            github_login = None



        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

        return render(request, 'core/settings.html', {
            'github_login': github_login,
            'can_disconnect': can_disconnect
        })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'customer_register/customer_form.html', {'form': form})


def customer_list(request):
    context = {'customer_list' : Customer.objects.all() }
    return  render(request, "customer_register/customer_list.html",context)

def customer_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
             customer = Customer.objects.get(pk=id)
             form = CustomerForm(instance=customer)
        return render(request, "customer_register/customer_form.html", {'form' : form})
    else:
        if id == 0:
           form  = CustomerForm(request.POST)
        else:
             customer = Customer.objects.get(pk=id)
             form = CustomerForm(request.POST,instance= customer)
        if form.is_valid():
               form.save()
        return redirect('/customer/list')

def customer_delete(request,id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/customer/list')