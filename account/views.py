
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html')

'''
 Sign Up view method
If user send GET request, we send UserRegistrationForm for him
If user submit the form, we'll recieve POST request, then we 
start to validation, if it was valid, we create User object.
'''
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)

            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
