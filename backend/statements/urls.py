from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Job_Statement_View_Set, Worker_Statement_View_Set

router = DefaultRouter()
router.register(r'jobs', Job_Statement_View_Set)
router.register(r'workers', Worker_Statement_View_Set)



urlpatterns = [
    path('', include(router.urls))
]
