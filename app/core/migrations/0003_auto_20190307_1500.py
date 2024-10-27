import datetime
from django.db import migrations, models
from django.utils.timezone import now  # Importando timezone.now

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo_completed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=now),  # Usando timezone.now
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(blank=True, max_length=280),
        ),
    ]
