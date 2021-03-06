from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Gamer(models.Model):
    avatar_name = models.CharField(max_length=200)
    playtime = models.IntegerField()
    money_spent = models.IntegerField()

    def __str__(self):
        return self.avatar_name