from django.db import models


# Create your models here.

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')


class Choice(BaseModel):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
