from django.db import models

class Pompe(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    id_cuve = models.ForeignKey('cuve.Cuve', on_delete=models.CASCADE)  # Assuming 'Cuve' is in the 'cuve' app
    id_pompiste = models.ForeignKey('pompiste.Pompiste', on_delete=models.CASCADE)  # Assuming 'Pompiste' is in the 'pompiste' app

    def __str__(self):
        return f"Pompe {self.id} - {self.type}"
