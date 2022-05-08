from django import forms
from django.forms import ModelForm

from .models import Report


class CvedesForm(forms.Form):
    cve_id = forms.CharField(max_length=15, required=False)

class BurptoSqlmap(forms.Form):
    burptosqlmap = forms.CharField(max_length=150)

class URLForm(forms.Form):
    target_url = forms.CharField(required=False)

class SubDomainForm(forms.Form):
    target_url = forms.CharField(required=False)

class CrawlForm(forms.Form):
    target_url = forms.CharField()
    cookie = forms.CharField(required=False)
    # user_agent = forms.CharField(required=False)


class IpscanForm(ModelForm):
    class Meta:
        model = Report
        fields = ["ip"]

class Exploitsqlmap(forms.Form):
    level = forms.CharField(max_length=15)
    risk = forms.CharField(max_length=15)
    database = forms.CharField()
    tamper = forms.CharField()