from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from back_office.models import PerfilUsuario, Reto, Beneficios, AdvertisementTool, PlanCompensacion


class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario


class UsuarioAdmin(UserAdmin):
    inlines = (PerfilUsuarioInline, )


admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)


class RetoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reto, RetoAdmin)


class BeneficiosAdmin(admin.ModelAdmin):
    pass

admin.site.register(Beneficios, BeneficiosAdmin)


class AdvertisementToolAdmin(admin.ModelAdmin):
    pass

admin.site.register(AdvertisementTool, AdvertisementToolAdmin)


class PlanCompensacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlanCompensacion, PlanCompensacionAdmin)