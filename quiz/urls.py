from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import index, test, QuizCreateView

urlpatterns = [
    path('', index),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('quiz/', test),
    path('quiz/create', QuizCreateView.as_view(), name='add'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)