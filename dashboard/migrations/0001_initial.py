# Generated by Django 4.1.3 on 2022-11-30 21:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Produto",
                "verbose_name_plural": "Produtos",
            },
        ),
        migrations.CreateModel(
            name="Vendedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Vendedor",
                "verbose_name_plural": "Vendedors",
            },
        ),
        migrations.CreateModel(
            name="Vendas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total", models.FloatField()),
                ("data", models.DateTimeField(default=datetime.datetime)),
                (
                    "nome_produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.produto",
                    ),
                ),
                (
                    "vendedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="dashboard.vendedor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Venda",
                "verbose_name_plural": "Vendas",
            },
        ),
    ]