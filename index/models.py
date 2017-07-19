from django.db import models


class Business(models.Model):
    caption = models.CharField(max_length=32, verbose_name='机房', null=True)
    code = models.CharField(max_length=32, null=True, default="SA", verbose_name='产品线', )

    class Meta:
        db_table = "Business"
        verbose_name = "机房组"
        verbose_name_plural = '机房组'

    def __str__(self):
        return self.caption


