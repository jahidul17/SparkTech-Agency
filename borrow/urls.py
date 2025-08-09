from django.urls import path
from .views import BorrowViewSet, ReturnBookView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'borrow', BorrowViewSet, basename='borrow')

urlpatterns = [
    path('return/', ReturnBookView.as_view()),

]