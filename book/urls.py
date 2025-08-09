from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .import views


router=DefaultRouter()

router.register('authors',views.AuthorViewSet)
router.register('categories',views.CategoriesViewSet)
router.register('books',views.BookViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('books/<int:pk>/', views.BookUpdateView.as_view(), name='bookupdate'),

]

