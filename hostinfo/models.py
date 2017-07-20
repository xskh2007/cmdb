from django.db import models

from  index.models import Business
# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=50, verbose_name='主机编号')
    ip = models.GenericIPAddressField(verbose_name='IP',null=True)
    port = models.CharField(max_length=50, verbose_name='端口',null=True)
    username = models.CharField(max_length=50, verbose_name='登陆用户',null=True)
    password = models.CharField(max_length=50, verbose_name='密码',null=True)
    jifang = models.ForeignKey(to=Business, to_field='id', null=True)


    osversion = models.CharField(max_length=50,verbose_name='系统版本',null=True)
    memory = models.CharField(max_length=50,verbose_name='内存',null=True)
    disk = models.CharField(max_length=50,verbose_name='硬盘',null=True)

    sn = models.CharField(max_length=50, verbose_name='SN', null=True)
    model_name = models.CharField(max_length=50, verbose_name='型号', null=True)
    cpu_core = models.CharField(max_length=50, verbose_name='CPU', null=True)
    beizhu = models.CharField(max_length=1000, verbose_name='备注', null=True)


    class  Meta:
        db_table ="Host"
        verbose_name="服务器"
        verbose_name_plural = '服务器'


    def __str__(self):
        return self.hostname


class History(models.Model):
    root = models.CharField(max_length=50, verbose_name='用户', null=True)
    ip = models.GenericIPAddressField(verbose_name='IP',null=True)
    port = models.CharField(max_length=50,verbose_name='端口',null=True)
    cmd = models.CharField(max_length=50,verbose_name='命令',null=True)
    user = models.CharField(max_length=50,verbose_name='操作者',null=True)
    ctime = models.DateTimeField(auto_now_add=True, null=True, verbose_name='时间')

    class  Meta:
        db_table ="history"
        verbose_name="历史命令"
        verbose_name_plural = '历史命令'


    def __str__(self):
        return self.user




