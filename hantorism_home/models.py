from django.db import models
from django.utils import timezone

GENDER_CHOICES=[
('male','Male'),
('female','Female'),
]
ISHANTOR_CHOICES=[
('hantor','YES'),
('no_hantor','NO'),
]

class User(models.Model):
    ID = models.CharField(max_length=20,
        primary_key=True,
        unique=True)
    PW = models.CharField(
        max_length=20)

    name = models.CharField(
        max_length=20)
    studentNum = models.CharField(max_length=10)
    major = models.CharField(
        max_length=20)

    gender = models.CharField(
        max_length=8,
        choices=GENDER_CHOICES)
    email = models.CharField(
        max_length=20)
    isHantor = models.CharField(
        max_length=10,
        choices=ISHANTOR_CHOICES)

    object=models.Manager()

class Post(models.Model):
    userID = models.ForeignKey(User,
        max_length=20,
        on_delete=models.CASCADE)
    title = models.CharField(
        max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )

    def publish(self):
        self.created_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    postNum=models.ForeignKey(Post,
        on_delete=models.CASCADE)
    userID=models.CharField(max_length=20)
    body=models.TextField()
    created_date=models.DateTimeField(
        default=timezone.now
    )

