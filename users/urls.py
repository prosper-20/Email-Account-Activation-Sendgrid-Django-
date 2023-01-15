from django.urls import path

from .views import (
    SignUpView,
    ActivateView,
    CheckEmailView,
    SuccessView,
)


# https://docs.djangoproject.com/en/4.0/ref/templates/language/#id1
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),
    path('check-email/', CheckEmailView.as_view(), name="check_email"),
    path('success/', SuccessView.as_view(), name="success"),
]