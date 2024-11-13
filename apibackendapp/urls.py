from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

#create an instance of the DefaultRouter class
router = DefaultRouter()

#register the mapping for url and views
# r for raw string - to escape special chars
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)

#creating the urls for the Login and Signup API views
#They are not Viewset, they are API views so it should be added to the 
#URL patterns list directly
urlpatterns = [
    path("signup/",views.SignupAPIView.as_view(), name="user-signup"),
    path("login/",views.LoginAPIView.as_view(), name="user-login"),
]

#append the router.urls to the already created urlpatterns
urlpatterns = urlpatterns + router.urls