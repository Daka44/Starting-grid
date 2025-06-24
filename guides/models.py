from django.db import models

class Guide(models.Model):
    title = models.CharField(max_length=200)                 #제목  
    summary = models.TextField(max_length=600)              #예문
    content = models.TextField()                               #내용
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title