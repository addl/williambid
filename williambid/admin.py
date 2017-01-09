from django.contrib import admin

# Register your models here.
from williambid.models import Articulo, Subasta, PaqueteBid


class ArticuloAdmin(admin.ModelAdmin):
    pass


admin.site.register(Articulo, ArticuloAdmin)


class PaqueteBidAdmin(admin.ModelAdmin):
    pass


admin.site.register(PaqueteBid, PaqueteBidAdmin)


class PujaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subasta, PujaAdmin)