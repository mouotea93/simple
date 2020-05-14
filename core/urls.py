from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('secret_page/', views.secret_page, name="secret_page"),
    path('upload/', views.upload, name="upload"),
    path('book_list/', views.book_list, name="book_list"),
    path('upload_book/', views.upload_book, name="upload_book"),
    path('delete_book/<int:pk>/', views.delete_book, name="delete_book"),
    path('accounts/', include('django.contrib.auth.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)