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

class HantorismLibrary(models.Model):
    book_user = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    book_owner = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    rent_date = models.DateTimeField(
            default=timezone.now)

    rental_status = models.BooleanField(default=False)

    def publish(self):
        self.rent_date = timezone.now()
        self.save()

    def __str__(self):
        return self.book_user