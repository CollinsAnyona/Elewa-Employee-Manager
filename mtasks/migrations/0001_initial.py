from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='description')),
                ('resolution', models.TextField(blank=True, max_length=2000, null=True, verbose_name='resolution')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='deadline')),
                ('state', models.CharField(choices=[('00-to-do', 'To Do'), ('10-in-progress', 'In Progress'), ('20-blocked', 'Blocked'), ('30-done', 'Done'), ('40-dismissed', 'Dismissed')], default='00-to-do', max_length=20, verbose_name='state')),
                ('priority', models.CharField(choices=[('00-low', 'Low'), ('10-normal', 'Normal'), ('20-high', 'High'), ('30-critical', 'Critical')], default='10-normal', max_length=20, verbose_name='priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users_created', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='partner.partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks_assigned', to=settings.AUTH_USER_MODEL, verbose_name='assigned to')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(max_length=200, verbose_name='description')),
                ('is_done', models.BooleanField(default=False, verbose_name='done?')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mtasks.task')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Check List',
            },
        ),
        migrations.AddIndex(
            model_name='task',
            index=models.Index(fields=['state', '-priority', '-deadline'], name='mtasks_task_priority_idx'),
        ),
    ]
