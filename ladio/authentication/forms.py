from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm

User = get_user_model()

class SuperuserAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Please enter the correct %(username)s and password "
                           "for a staff account. Note that both fields may be "
                           "case-sensitive."
    }
    required_css_class = 'required'

    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_superuser:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )

class StaffAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Please enter the correct %(username)s and password "
                           "for a staff account. Note that both fields may be "
                           "case-sensitive."
    }
    required_css_class = 'required'

    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_staff:
            raise forms.ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'username': self.username_field.verbose_name}
            )

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'nickname', 'is_staff', 'groups',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname', 'is_staff', 'is_superuser', 'groups', )

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]