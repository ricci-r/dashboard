from django.contrib import admin

from .models import Produto, Vendas, Vendedor

admin.site.register(Produto)
admin.site.register(Vendas)
admin.site.register(Vendedor)
