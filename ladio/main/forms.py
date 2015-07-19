from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth import get_user_model
from main.models import Channel, Content

User = get_user_model()

class ChannelAdminForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), initial=0)

    class Meta:
        model = Channel
        fields = ('user', 'ch_name', 'bg_img', 'brief', 'intro')

