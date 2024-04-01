from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логін:",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Логін користувача"}
            )
        )
    password = forms.CharField(
        label="Пароль:",
        max_length=100,
        required=False,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Пароль користувача"}
            )
        )
    remember_me = forms.BooleanField(
        label="Запам'ятати мене",
        required=False,
        widget=forms.CheckboxInput
        )


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label="Текучий пароль:",
        max_length=100,
        required=False,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Введіть текучий пароль"}
            )
        )
    new_password = forms.CharField(
        label="Новий пароль:",
        max_length=100,
        required=False,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Введіть новий пароль"}
            )
        )
    confirm_password = forms.CharField(
        label="Підтвердити пароль:",
        max_length=100,
        required=False,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Підтвердіть новий пароль"}
            )
        )


class AddUserForm():
    pass


class AddGroupForm():
    pass


class ShowUserProfileForm():
    pass
