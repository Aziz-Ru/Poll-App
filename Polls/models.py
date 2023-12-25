from django.db import models

class Question(models.Model):
    question_txt=models.CharField(max_length=100,null=True)
    option_one=models.CharField(max_length=50,null=True)
    option_two=models.CharField(max_length=50,null=True)
    option_three=models.CharField(max_length=50,null=True)
    option_four=models.CharField(max_length=50,null=True)
    votes_one=models.IntegerField(default=0)
    votes_two=models.IntegerField(default=0)
    votes_three=models.IntegerField(default=0)
    votes_four=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.question_txt

class User(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)

