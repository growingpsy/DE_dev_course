from polls.models import Question
from polls_api.serializers import QuestionSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserList(generics.ListAPIView): # User 목록 조회
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView): # 단일 User 상세 조회
    queryset = User.objects.all()
    serializer_class = UserSerializer