from django.db import migrations, models
from django.utils.timezone import now  # Importando timezone.now


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_auto_20190307_1500"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateField(blank=True, default=now),  # Usando timezone.now
        ),
    ]
