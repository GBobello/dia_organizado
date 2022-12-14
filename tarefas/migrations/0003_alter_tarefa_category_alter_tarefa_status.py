# Generated by Django 4.0.6 on 2022-08-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0002_alter_tarefa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='category',
            field=models.CharField(choices=[('urgente', 'Urgente'), ('importante', 'Importante'), ('precisa ser feito', 'Precisa ser feito')], default='importante', max_length=25),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(choices=[('concluído', 'Concluído'), ('pendente', 'Pendente'), ('adiado', 'Adiado')], default='pendente', max_length=25),
        ),
    ]
