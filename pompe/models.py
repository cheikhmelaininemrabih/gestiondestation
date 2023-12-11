from django.db import models

class Pompe(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, null= True)
    model = models.CharField(max_length=100, null= True)
    id_cuve = models.ForeignKey('cuve.Cuve', on_delete=models.CASCADE)  
    is_active = models.BooleanField(default=True, null= True)
    id_pompiste = models.ForeignKey('pompiste.Pompiste', on_delete=models.CASCADE, related_name='pompes' , null=True , blank=True )
    def __str__(self):
        return f"Pompe {self.id} - {self.type}"
