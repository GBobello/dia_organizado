# Generated by Django 4.0.6 on 2022-08-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('urgente', 'Urgente'), ('importante', 'Importante'), ('adiado', 'Adiado')], default='importante', max_length=25)),
                ('status', models.CharField(choices=[('concluído', 'Concluído'), ('pendente', 'Pendente'), ('adiado', 'Adiado')], default='pendente', max_length=25)),
            ],
        ),
    ]
