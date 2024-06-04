from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text = ""
            self.fields[field_name].widget.attrs.update({'placeholder': ''})