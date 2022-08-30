from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    birth = models.DateField()
    user_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user_id

class Review(models.Model):
    user_id = models.ForeignKey("User",on_delete=models.CASCADE, db_column="user_id")

    title = models.CharField(max_length=30)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    star = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    companyName = models.CharField(max_length=40)
    licenseDate = models.CharField(max_length=30)