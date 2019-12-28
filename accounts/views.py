from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import Registration
from .models import AlumniProfile, ImageSlider, JobOpenings, Account, Events
from .forms import JobUpdate, UserDetails, UserProfile
from .models import Account as User, BestAlumnis
from django.contrib.auth.decorators import login_required


def index(request):
    sliders = ImageSlider.objects.filter()
    best_alumnis = BestAlumnis.objects.filter()
    img1 = sliders[0].event_image.url
    img2 = sliders[1].event_image.url
    img3 = sliders[2].event_image.url
    events = list(Events.objects.filter())[-3:]
    return render(request, 'accounts/index.html', {"img1": img1,
                                                   "img2": img2,
                                                   "img3": img3,
                                                   "alumnis": best_alumnis,
                                                   "events": events,
                                                   })


def signin(request):
    message = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Login Successfull")
                return redirect('/')
            else:
                message = "invalid email or password"
                messages.error(request, "Invalid Username or Password")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form, "message": message})


def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"New Account Created")
            login(request, user)
            print(form)
            print(form.cleaned_data.get('username'))
            print(form.cleaned_data.get('email'))
            return redirect('/')
    else:
        form = Registration()
    return render(request, "accounts/registration.html", {"form": form})


def about(request):
    return render(request, "accounts/about.html")


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("/")


@login_required
def profile(request):
    if request.method == "POST":
        details = UserDetails(request.POST, request.FILES, instance=request.user)
        if details.is_valid():
            details.save()
            print(request.POST)
            messages.success(request, "Successfully Information Update")
            return redirect('/profile')
    else:
        pass
    details = UserDetails(instance=request.user)
    user_details = Account.objects.get(email=request.user)
    print("department: ", request.user.dept)
    fellows = Account.objects.filter(pass_out_batch=request.user.pass_out_batch, dept=request.user.dept)
    print("Fellows ", fellows)
    return render(request, "accounts/profile.html",
                  {
                      "user_details": user_details,
                      "details": details,
                      "fellows": fellows,
                  })


@login_required
def job_post(request):
    if request.method == "POST":
        form = JobUpdate(data=request.POST)
        print("afdasfsdffa")
        if form.is_valid():
            print('form:data', form)
            form.save()
            messages.success(request, "Post Updated Successfully")
            return redirect("/profile")
        else:
            messages.error(request, "failed to store")

    details = JobUpdate()
    return render(request, "accounts/jobopening.html",
                  {
                      "details": details
                  })


def job_view(request):
    jobs = JobOpenings.objects.filter()
    return render(request, "accounts/display_job.html",
                  {
                      "jobs": jobs,
                  })


def forgot_pass(request):
    return render(request, "accounts/password_reset.html")


def events(request):
    events = list(Events.objects.filter())[::-1]
    return render(request, "accounts/events.html", {"events": events})
