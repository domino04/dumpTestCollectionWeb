from django.db import models

# Create your models here.
class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name =  models.CharField(max_length=200)
    total_score = models.CharField(max_length=3)
    pass_score = models.CharField(max_length=3)
    per_score = models.CharField(max_length=2)
    regist_link = models.CharField(max_length=1000)
    created_date = models.DateTimeField('date published')

    def __str__(self):
        return self.test_name


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)
    multiple_answer_yn = models.CharField(max_length=1)
    question_answer = models.CharField(max_length=1)
    question_answer_second = models.CharField(max_length=1)
    created_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_order = models.CharField(max_length=1)
    choice_text = models.CharField(max_length=1000)
    created_date = models.DateTimeField('date published')

    def __str__(self):
        return self.choice_text