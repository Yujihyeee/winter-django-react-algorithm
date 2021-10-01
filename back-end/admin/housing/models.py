from django.db import models


class Housing(models.Model):
    use_in_migrations = True
    id = models.CharField(primary_key=True, max_length=10)
    longitude = models.AutoField()
    latitude = models.AutoField()
    housing_median_age = models.AutoField()
    total_rooms = models.AutoField()
    total_bedrooms = models.AutoField()
    population = models.AutoField()
    households = models.AutoField()
    median_income = models.AutoField()
    median_house_value = models.AutoField()
    ocean_proximity = models.AutoField()

    class Meta:
        db_table = ''

    def __str__(self):
        return f'[{self.pk}] {self.id}'

