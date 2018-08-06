from django.db import models


# Create your models here.
class users(models.Model):
    id = models.AutoField
    uin = models.CharField(null=False, max_length=11)
    phone = models.CharField(null=False, max_length=11)
    points = models.IntegerField(null=False, max_length=11)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_created=True)

    def deductPoints(self, qq, points):
        user = users.objects.get(qq=qq)
        if user.points <= 0:
            return False
        user.points -= points
        user.save()
        return True


class cookies(models.Model):
    id = models.AutoField
    eleme_key = models.CharField(null=False, max_length=255)
    url_appand = models.CharField(null=False, max_length=255)
    phone = models.CharField(null=False, max_length=11)
    used_times = models.IntegerField(null=False, default=0, max_length=10)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_created=True)

    def getEleme_key(self):
        return self.eleme_key

    def getNextId(self):
        cookie = cookies.objects.order_by('used_times', 'id').first()
        return cookie.id
