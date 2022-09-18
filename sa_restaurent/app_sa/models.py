from django.db import models
# foodExercise is name of the table 
class foodExercise(models.Model): 
    Cname = models.CharField(max_length=50)
    Clname = models.CharField(max_length=50)
    Cemail = models.CharField(max_length=50)
    Cphone = models.IntegerField()
    Cno_people = models.IntegerField()
    Cenquiry = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.Cname
