from django.contrib import admin
from .models import cookies
from .models import users
from .models import kami
# Register your models here.


admin.site.register(cookies)
admin.site.register(users)
admin.site.register(kami)