from django.core.validators import MaxValueValidator
from django.db import models
from datetime import datetime

class Davlat(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Club(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="clublar/")
    prezident = models.CharField(max_length=255, blank=True, null=True)
    trener = models.CharField(max_length=255)
    t_sana = models.DateField(blank=True, null=True)
    kapital = models.PositiveIntegerField(blank=True, null=True)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Pozitsiya(models.Model):
    nom = models.CharField(max_length=255)
    turi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.turi} {self.nom}"


class Player(models.Model):
    ism = models.CharField(max_length=255)
    raqam = models.PositiveSmallIntegerField(validators=[MaxValueValidator(99)])
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    t_sana = models.DateField(blank=True, null=True)
    maosh = models.PositiveIntegerField(blank=True, null=True)
    narx = models.PositiveIntegerField()
    davlat = models.ForeignKey(Davlat, on_delete=models.SET_NULL, null=True)
    possitsiya = models.ForeignKey(Pozitsiya, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.ism

    def yosh(self):
        h_yil = datetime.now().year
        t_yil = int(str(self.t_sana)[:4])

        return h_yil - t_yil






