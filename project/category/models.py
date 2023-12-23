from django.db import models

class Model(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    address = models.TextField()
    father_name = models.TextField(default="Rahim")
    full_name = models.CharField(max_length=100)
    auto = models.AutoField(primary_key=True)
    date = models.DateField()
    date_time = models.DateTimeField()
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    email = models.EmailField()
    float = models.FloatField()
    foreign_key = models.ForeignKey('self', on_delete=models.CASCADE)
    generic_ip_address = models.GenericIPAddressField()
    integer = models.IntegerField()

    
