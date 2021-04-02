from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
class questions(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse ('questions-detail',kwargs = {'pk': self.pk})


class answers(models.Model):
    
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    of_question = models.ForeignKey(questions,on_delete=models.CASCADE)
    upvote = models.ManyToManyField(User,related_name = 'likes', blank = True)
    downvote = models.ManyToManyField(User,related_name = 'dislikes', blank = True)
    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse ('questions-detail',kwargs = {'pk': self.pk})

    
# class upvote(models.Model):
# author = models.ForeignKey(User, on_delete=models.CASCADE)
# of_answer = models.ForeignKey(answers,on_delete=models.CASCADE,related_name='upvotes')
# count = models.IntegerField(default=0)

# class downvote(models.Model):
# author = models.ForeignKey(User, on_delete=models.CASCADE)
# of_answer = models.ForeignKey(answers,on_delete=models.CASCADE,related_name='downvotes')
# count = models.IntegerField(default=0)

