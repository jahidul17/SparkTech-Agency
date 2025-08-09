from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.contrib.auth.models import User
from .models import Borrow
from .serializers import BorrowSerializer
from book.models import Book
from datetime import timedelta
from django.utils import timezone

class BorrowViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        borrows = Borrow.objects.filter(user=request.user, return_date__isnull=True)
        serializer = BorrowSerializer(borrows, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def create(self, request):
        book_id = request.data.get('book_id')
        if not book_id:
            return Response({'error': 'book_id required'}, status=400)
        try:
            book = Book.objects.select_for_update().get(id=book_id)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=404)
        active_borrows = Borrow.objects.filter(user=request.user, return_date__isnull=True).count()
        if active_borrows >= 3:
            return Response({'error': 'Borrowing limit reached'}, status=400)
        if book.available_copies < 1:
            return Response({'error': 'Book not available'}, status=400)
        borrow = Borrow.objects.create(
            user=request.user,
            book=book,
            due_date=timezone.now() + timedelta(days=14)
        )
        book.available_copies -= 1
        book.save()
        return Response(BorrowSerializer(borrow).data, status=201)

class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):
        borrow_id = request.data.get('borrow_id')
        if not borrow_id:
            return Response({'error': 'borrow_id required'}, status=400)
        try:
            borrow = Borrow.objects.select_for_update().get(id=borrow_id, user=request.user, return_date__isnull=True)
        except Borrow.DoesNotExist:
            return Response({'error': 'Active borrow not found'}, status=404)
        borrow.return_date = timezone.now()
        late_days = (borrow.return_date - borrow.due_date).days

        borrow.save()
        book = borrow.book
        book.available_copies += 1
        book.save()
         
        return Response({'message': 'Book returned'})
