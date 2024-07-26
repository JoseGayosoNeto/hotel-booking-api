from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import CustomUser, Employee, Guest

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "date_of_birthday", "gender",
                  "phone_number", "address", "postal_code", "city", "country",)


class EmployeeCreationForm(CustomUserCreationForm):

    class Meta:
        model = Employee
        fields = CustomUserCreationForm.Meta.fields + ("role", "hotel", "salary",)

class GuestCreationForm(CustomUserCreationForm):

    class Meta:
        model = Guest
        fields = CustomUserCreationForm.Meta.fields + ("passport_number",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "date_of_birthday", "gender",
                  "phone_number", "address", "postal_code", "city", "country",)

class EmployeeChangeForm(CustomUserChangeForm):

    class Meta:
        model = Employee
        fields = CustomUserChangeForm.Meta.fields + ("role", "hotel", "salary",)

class GuestChangeForm(CustomUserChangeForm):

    class Meta:
        model = Guest
        fields = CustomUserChangeForm.Meta.fields + ("passport_number",)
