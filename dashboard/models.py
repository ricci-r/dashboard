import datetime

from django.db import models


class Produto(models.Model):
    """Model definition for Produto."""
    nome = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Produto."""

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self) -> str:
        """Unicode representation of Produto."""
        return self.nome


class Vendedor(models.Model):
    """Model definition for Vendedor."""

    nome = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Vendedor."""

        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self) -> str:
        """Unicode representation of Vendedor."""
        return self.nome


class Vendas(models.Model):
    """Model definition for Vendas."""

    nome_produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    data = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        """Meta definition for Vendas."""

        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        """Unicode representation of Vendas."""
        return self.nome_produto.nome
