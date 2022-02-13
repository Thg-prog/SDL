from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст статьи')
    pub_date=models.DateTimeField("Дата публикации")
    cover=models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.title


class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name=models.CharField('Имя автора',max_length=50)
    author_text=models.TextField('Текст комментария')
