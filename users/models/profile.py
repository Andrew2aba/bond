from django.db import models


class Profile(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    memberSince = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=10, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"