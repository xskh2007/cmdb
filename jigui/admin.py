from django.contrib import admin

from jigui import  models


class  jigui(admin.ModelAdmin):
    search_fields = ('name','dx','yong') ## 定义搜索框以哪些字段可以搜索
    list_display = ('name','jq','zy','ziy','xz')#  每行的显示信息
    list_display_links = ('name',)
    list_filter = ('yong',)
admin.site.register(models.JiguiInfo,jigui)
admin.site.register(models.dx)