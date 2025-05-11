from django.urls import path
from .admin import custom_admin_site
from .views import login_view

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('login/', login_view, name='login'),
    # Other URL patterns
]