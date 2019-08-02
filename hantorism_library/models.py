from django.db import models
from django.utils import timezone

# 도서관에서 필요한 모델
#
# book
# -책이름
# -책 소유자
# -대여상태
# -빌린 사람 이름
# -대여 날짜

#userID = models.ForeignKey(HantorismUser, on_delete = models.CASCADE)
from common_hantorism.models import HantorismUser

class Book(models.Model):
    book_name = models.CharField(max_length=20)
    book_rent_state = models.BooleanField(default = False)
    rent_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book_name

class BookOwner(models.Model):
    book_owner_name = models.CharField(max_length=20)
    book_owner = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)

    # def book_owner_(self):
    #     self.book_owner = models.
    #여기가 다른 모델에서 이름으로 찾아서 저장하는곳
    def __str__(self):
        return self.book_owner_name
class BookUser(models.Model):
    book_user_name = models.CharField(max_length=20)
    book_user = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    # def book_user_(self):
    #     self.book_owner = models.
    # 여기가 다른 모델에서 이름으로 찾아서 저장하는곳2

    def __str__(self):
        return self.book_user_name
