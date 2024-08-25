from django.db import migrations, models
from django.utils.timezone import now  # Importa timezone.now


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_auto_20190321_2123"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateField(blank=True, default=now),  # Usando timezone.now
        ),
    ]
