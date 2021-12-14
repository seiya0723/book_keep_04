from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class Category(models.Model):

    class Meta:
        db_table = "category"

    name    = models.CharField(verbose_name="カテゴリ名",max_length=20)
    income  = models.BooleanField(verbose_name="収入フラグ",default=False)
    user    = models.ForeignKey(User, verbose_name="投稿者", on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.name

class Balance(models.Model):

    class Meta:
        db_table = "balance"

    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)
    pay_date    = models.DateField(verbose_name="決済日")
    category    = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.PROTECT)
    value       = models.IntegerField(verbose_name="金額") 
    user        = models.ForeignKey(User, verbose_name="投稿者", on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.category.name
