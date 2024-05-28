"""
URL configuration for booksproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import  settings

# from .views import add_to_cart, view_cart, remove_from_cart

from bookapp.views import home,feed_back,login_view,login_user, contact, register, logout_user,sell_books
# from .views import home,demoo
urlpatterns = [

    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("login_view/",login_view,name="login_view"),
    path("login_user/",login_user,name="login_user"),
    path("register/", register, name="register"),
    path("logout/",logout_user,name="logout_user"),
    path("contact/",contact,name = "contact"),
    path('feed_back/',feed_back,name="feed_back"),
    # path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    # path('cart/', view_cart, name='view_cart'),
    # path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path("sell_books/",sell_books,name = "sell_books"),
    # path('', include('bookapp.urls')),  # Include the app's URLs
]                       





urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
