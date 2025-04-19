from django.db import models

# Create your models here.
# 모델 생성
# 모델을 테이블에 사용하기 위한 마이그레이션을 만든다
# 이 모델에 맞는 테이블을 만든다

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'제목: {self.question_text}, 날짜: {self.pub_date}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)