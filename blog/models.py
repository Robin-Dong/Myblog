from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField('分类', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField('标签', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "博客标签"
        verbose_name_plural = verbose_name


class Entry(models.Model):
    title = models.CharField('文章标题', max_length=128)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name='博客配图')
    body = models.TextField('正文')
    abstract = models.TextField('摘要', max_length=256, blank=True, null=True)
    visiting = models.PositiveIntegerField(default=0, verbose_name='访问量')
    category = models.ManyToManyField('Category', verbose_name="分类")
    tags = models.ManyToManyField('Tag', verbose_name='标签')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:blog_detail',kwargs={'blog_id': self.id})

    def increase_visiting(self):
        self.visiting += 1
        self.save(update_fields=['visiting'])
