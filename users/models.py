from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/')
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def get_image_url(self):
        try:
            return self.image.url
        except:
            return ''

@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
