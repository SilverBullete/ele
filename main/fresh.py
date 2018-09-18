from .models import cookie
def fresh():
    cooks = cookie.objects.all()
    for i in cooks:
        # if i.used_times < 10:
        i.used_times = 0
        i.save()

