from polls.models import Question
from polls_api.serializers import QuestionSerializer, UserSerializer, RegisterSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # 읽기는 누구나, 쓰기는 로그인만 허용
    
    def perform_create(self, serializer): # POST 요청 시 자동으로 작성자를 현재 로그인 사용자로 지정
        serializer.save(owner=self.request.user)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView): # User 목록 조회
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView): # 단일 User 상세 조회
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterUser(generics.CreateAPIView): # User 등록
    serializer_class = RegisterSerializer