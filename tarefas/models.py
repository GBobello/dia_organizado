from django.db import models

# - descrição
# - data de criação
# - categoria /urgente, importante ou precisa ser feito/
# - status /concluida, pendente ou adiado/


class Tarefa(models.Model):
    OPTIONS_STATUS = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )

    OPTIONS_CATEGORY = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )

    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=25, choices=OPTIONS_CATEGORY, default='importante')
    status = models.CharField(
        max_length=25, choices=OPTIONS_STATUS, default='pendente')

    def __str__(self):
        return u'%s' % self.description
