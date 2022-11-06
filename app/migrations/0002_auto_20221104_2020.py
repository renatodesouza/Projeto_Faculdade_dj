# Generated by Django 3.2 on 2022-11-04 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregaatividade',
            name='nota',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='entregaatividade',
            name='resposta',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='entregaatividade',
            name='status',
            field=models.CharField(choices=[('EN', 'Entregue'), ('CO', 'Corrigido'), ('PE', 'Pendente')], default='PE', max_length=2),
        ),
    ]
