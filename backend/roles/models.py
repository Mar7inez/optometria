from django.db import models


class RolModel(models.Model):
    rol = models.CharField(max_length=50, null=False, blank=False, verbose_name="Rol")

    def __str__(self):
        return self.rol
    
    def __repr__(self):
        return f"<Rol: {self.rol}>"
    
    class Meta:
        db_table = "roles"
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        ordering = ["pk"]