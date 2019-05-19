from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('martor/', include('martor.urls')),
    path('', include('home.urls')),
    path('register/', account_views.Register, name='Register'),
    path('accounts/', account_views.Account, name='Account'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='Logout'),
    path('blog/', include('blog.urls')),
    path('about/', include('contact.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'home.views.error404'
