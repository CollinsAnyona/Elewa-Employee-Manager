from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtasks', '0001_initial'),
    ]

    # No real DB changes
    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
