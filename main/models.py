from django.db import models


# Create your models here.
class users(models.Model):
    id = models.AutoField
    qq = models.CharField(null=False, max_length=11)
    phone = models.CharField(null=False, max_length=11)
    points = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True)


class cookie(models.Model):
    id = models.AutoField
    eleme_key = models.CharField(null=False, max_length=255)
    url_appand = models.CharField(null=False, max_length=255)
    track_id = models.CharField(null=False, max_length=255)
    cookie = models.CharField(null=False, max_length=2000)
    phone = models.CharField(null=False, max_length=11)
    qq = models.CharField(null=False, max_length=20)
    used_times = models.IntegerField(null=False, default=0)

    def getNextId(self):
        cook = cookie.objects.order_by('used_times', 'id').first()
        return cook.id


class cookies(models.Model):
    id = models.AutoField
    eleme_key = models.CharField(null=False, max_length=255)
    url_appand = models.CharField(null=False, max_length=255)
    phone = models.CharField(null=False, max_length=11)
    used_times = models.IntegerField(null=False, default=0)

    def getNextId(self):
        cookie = cookies.objects.order_by('used_times', 'id').first()
        return cookie.id


class kami(models.Model):
    id = models.AutoField
    kami = models.CharField(null=False, max_length=12)
    val = models.IntegerField(null=False)
    used = models.IntegerField(null=False, default=0)


class logs(models.Model):
    id = models.AutoField
    qq = models.CharField(null=False, max_length=11)
    money = models.CharField(null=False, max_length=11)
