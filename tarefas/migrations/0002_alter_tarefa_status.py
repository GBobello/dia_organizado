# Generated by Django 4.0.6 on 2022-08-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(choices=[('concluído', 'Concluído'), ('pendente', 'Pendente'), ('precisa ser feito', 'Precisa ser feito')], default='pendente', max_length=25),
        ),
    ]
