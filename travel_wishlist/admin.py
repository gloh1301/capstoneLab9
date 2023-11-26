from django.contrib import admin
from .models import Place, CatFact

# sets up the admin version of the site
admin.site.register(Place)
admin.site.register(CatFact)
