from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #owner를 설정한다 + relatedname -> user.profile로 접근 가능
    image = models.ImageField(upload_to='profile/', null=True)
    #image를 저장할 수 있는 필드 -> upload_to: 저장할 위치 지정 media/profile/에 저장
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)
