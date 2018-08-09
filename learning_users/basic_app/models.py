from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE) #not inheriting user but refering indirectly
    #additional attributes
    portfolio = models.URLField(blank = True)
    picture = models.ImageField(upload_to = 'profile_pics', blank = True)

    def __str__(self):
        return self.user.username
