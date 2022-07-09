
from django.contrib.auth.forms import UserCreationForm   # type: ignore
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

