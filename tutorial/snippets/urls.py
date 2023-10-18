from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('snippets/', views.snippet_list.as_view()),
    path('snippets/<int:pk>/', views.snippet_detail.as_view()),
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
