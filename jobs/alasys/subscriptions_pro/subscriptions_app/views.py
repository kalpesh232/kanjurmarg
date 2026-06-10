from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserSubscription
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

@login_required
def subscription_details(request):
    sub,_ = UserSubscription.objects.get_or_create(user = request.user)
    print("sub : ", sub)
    print("_ : ", _)
    sub.ensure_renewed()
    return render(request,"details.html",{"sub" : sub})

@login_required
def perform_action(request, cost):
    sub, _ = UserSubscription.objects.get_or_create(user=request.user)
    if sub.deduct(cost):
        messages.success(request, f"Action allowed. {cost} credits used.")
    else:
        messages.error(request, "Not enough credits.")
    return redirect("subscription_details")

@login_required
def recharge_credits(request):
    if request.method == "POST":
        try:
            amount =  int(request.POST.get("amount",0))
            if amount > 0 :
                sub, _ = UserSubscription.objects.get_or_create(user=request.user)
                sub.recharge(amount)
                messages.success(request, f"{amount} credits added.")
            else:
                messages.error(request,"Enter positive credits.")
        except ValueError:
            messages.error(request, "Invalid amount.")
        return redirect("subscription_details")
    return render(request, "recharge.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form' : form})

def profile(request):
    return HttpResponse("User Profile Page")