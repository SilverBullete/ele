from .models import cookies

def fresh():
    cooks = cookies.objects.all()
    for i in cooks:
        if i.used_times < 10:
            i.used_times = 0
            i.save()
