from django.db import models


class User(models.Model):
    dni = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Project(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    link = models.URLField()
    skills = models.ManyToManyField('Skill', through='Usage')

class Skill(models.Model):
    DATABASE = 'DB'
    TOOL = 'T'
    FRAMEWORK = 'F'
    LANGUAGE = "L"
    PROGRAMMING_LANGUAGE = "PL"
    CLOUD_COMPUTING = "CC"

    TYPE_CHOICES = [
        (DATABASE, 'Database'),
        (TOOL, 'Tool'),
        (FRAMEWORK, 'Framework'),
        (LANGUAGE, 'Language'),
        (PROGRAMMING_LANGUAGE, 'Programming Language'),
        (CLOUD_COMPUTING, 'Cloud Computing'),
    ]
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    level = models.IntegerField()
    years_of_experience = models.FloatField()
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=LANGUAGE,
    )

class Usage(models.Model):
    percentage = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
