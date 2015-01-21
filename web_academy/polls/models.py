from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
    	return 'Question  {} at {}'.format(self.question_text,self.pub_date)

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField('date of birth')
    contacts = models.EmailField(max_length=75)
