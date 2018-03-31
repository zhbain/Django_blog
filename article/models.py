from django.db import models

# Create your models here.

class Article(models.Model) :
    #文章标题
    title = models.CharField(max_length = 100)  
    #文章标签
    category = models.CharField(max_length = 50, blank = True)
    #文章日期
    date_time = models.DateTimeField(auto_now_add = True)
    #文章正文
    content = models.TextField(blank = True, null = True)

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']