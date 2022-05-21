from django.db import models

from genders.models import GenderModel


class Patient(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombre")
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Apellido")
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="Email")
    gender = models.OneToOneField(GenderModel, on_delete=models.SET_NULL, null=True, verbose_name="Género")

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
    def __repr__(self):
        return f"<Patient: {self.last_name}, {self.first_name}>"
    
    class Meta:
        db_table = "patients"
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["pk"]