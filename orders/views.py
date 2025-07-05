from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PhoneVerificationForm, OrderCreateForm
from account.models import StoreUser
from .models import OrderItem, Order
from cart.cart import Cart
import random
from cart.common.KaveSms import send_sms_with_template
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse
import requests
import json


def verify_phone(request):
    if request.user.is_authenticated:
        return redirect('orders:order_create')
    if request.method == 'POST':
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if StoreUser.objects.filter(phone=phone).exists():
                messages.error(request, 'this phone is already registered.')
                return redirect('orders:verify_phone')
            else:
                tokens = {'token': ''.join(random.choices('0123456789', k=6))}
                request.session['verification_code'] = tokens['token']
                request.session['phone'] = phone
                send_sms_with_template(phone, tokens, 'verify')
                messages.error(request, 'verification code sent successfully.')
                return redirect('orders:verify_code')
    else:
        form = PhoneVerificationForm()
    return render(request, 'verify_phone.html', {'form': form})


def verify_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code:
            verification_code = request.session['verification_code']
            phone = request.session['phone']
            if code == verification_code:
                user = StoreUser.objects.create(phone=phone)
                user.set_password('123456')
                user.save()
                login(request, user)
                del request.session['verification_code']
                del request.session['phone']
                return redirect('store:product_detail')
            else:
                messages.error(request, 'verification code failed.')
    return render(request, 'verify_code.html')


