from django.db import models
from django.contrib.auth.models import User

class book(models.Model):
    title = models.CharField(max_length=200, verbose_name="書名")
    author = models.CharField(max_length=100, verbose_name="作者")
    isbn = models.CharField("ISBN",max_length=13, unique=True)
    published_date = models.DateField(null=True, blank=True, verbose_name="出版日期")
    
    def __str__(self):
        return f"{self.title} ({self.author})"


class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="借閱者")
    book = models.ForeignKey(book, on_delete=models.CASCADE, verbose_name="借閱書籍")
    borrow_date = models.DateField(auto_now_add=True, verbose_name="借閱日期")
    return_date = models.DateField(null=True, blank=True, verbose_name="歸還日期")

    def __str__(self):
        return f"{self.user.username} 借閱《{self.book.title}》"

    class Meta:
        verbose_name = "借閱紀錄"
        verbose_name_plural = "借閱紀錄管理"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return f"{self.user.username} 的個人資料"