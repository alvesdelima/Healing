from django.contrib import admin
from .models import Especialidade, DadosMedico, DatasAbertas
from paciente.models import Consulta, Documento

# Register your models here.

admin.site.register(Especialidade)
admin.site.register(DadosMedico)
admin.site.register(DatasAbertas)
admin.site.register(Consulta)
admin.site.register(Documento)
