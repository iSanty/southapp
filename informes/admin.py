from django.contrib import admin



from .models import GlobalPK, NombrePlanilla, SubClientes, PersonalDeposito, SectorDepo, Pendientes, PendientesArm, PendientePkPorDia, PenditenteArmPorDia, FinalizadoPkPorDia, FinalizadoArmPorDia
admin.site.register(GlobalPK)
admin.site.register(NombrePlanilla)
admin.site.register(SubClientes)
admin.site.register(PersonalDeposito)
admin.site.register(SectorDepo)
admin.site.register(Pendientes)
admin.site.register(PendientesArm)
admin.site.register(PendientePkPorDia)
admin.site.register(PenditenteArmPorDia)
admin.site.register(FinalizadoPkPorDia)
admin.site.register(FinalizadoArmPorDia)