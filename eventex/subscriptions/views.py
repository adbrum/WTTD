from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription

new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject='Confirmação de inscrição')

detail = DetailView.as_view(model=Subscription)
