from django.contrib import admin
from .models import Personnel
from .models import Equipe
from .models import Detail
from .models import Service
from .models import Projet
admin.site.register(Projet)
admin.site.register(Service)
admin.site.register(Detail)
admin.site.register(Equipe)
admin.site.register(Personnel)
# Register your models here.
