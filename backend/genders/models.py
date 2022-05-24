from django.db import models


class GenderModel(models.Model):
    type = models.CharField(max_length=20, null=False, blank=False, verbose_name="Tipo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    def __str__(self):
        return self.type
    
    def __repr__(self):
        return f"<Gender: {self.type}>"
    
    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["pk"]
    
    @classmethod
    def get_headers(cls):
        return ["Tipo"]