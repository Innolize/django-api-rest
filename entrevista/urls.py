from book.views import author_list_view, library_view, library_filter, book_view, book_search, leads_view

"""entrevista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin', admin.site.urls),
    path('api/library/<int:id>',  library_view,
         name='test'),  # GET, #POST, #PUT
    path('api/library/<int:library_id>/books/<int:book_id>',
         library_filter, name='library_filter'),  # GET
    path('api/book/<int:id>',  book_view,
         name='book_view'),  # GET, #POST, #PUT
    path('api/book/search',  book_search,
         name='book_search'),  # GET este tiene query param
    path('api/author/<int:id>',  author_list_view,
         name='author_list_view'),  # GET #POST #PUT
    path('api/library/lead',  leads_view, name='leads_view')  # POST

]
