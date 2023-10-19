from django.urls import include, path
from snippets import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

#METHOD 1 WITH MODELVIEWSET

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'users', views.UserViewSet,basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

#DEFINE THE METHODS\
# snippet_list = views.SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = views.SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_list = views.UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = views.UserViewSet.as_view({
#     'get': 'retrieve'
# })
# #ADD TO THE URL
# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])


#OLD, WITH GENERIC API VIEW AND OTHER
# urlpatterns = [
#     #GENERIC AND API VIEWS
#     path('snippets/', views.snippet_list.as_view(),name='snippet-list'),
#     path('snippets/<int:pk>/', views.snippet_detail.as_view(),name='snippet-detail'),
#     path('users/', views.UserList.as_view(),name='user-list'),
#     path('users/<str:username>/', views.UserDetail.as_view(),name='user-detail'),
#     path('', views.api_root), #entrypoint for out api
#     #OLD
#     #path('<int:pk>/', views.UserDetail.as_view()),
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),
    
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)
