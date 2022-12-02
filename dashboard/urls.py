from django.urls import path

from . import views

app_name = 'dashoard'

urlpatterns = [
    path('', views.index, name='home'),
    path('total-vendas', views.retorna_total_vendido, name='retorna_total_vendido'),
    path('total-faturamento', views.relatorio_faturamento, name='relatorio_faturamento'),
    path('total-produtos', views.relatorio_produtos, name='relatorio_produtos'),
    path('total-vendedor', views.relatorio_funcionarios, name='relatorio_funcionarios'),
]