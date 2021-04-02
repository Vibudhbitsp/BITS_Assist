# Generated by Django 3.1.6 on 2021-03-14 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BITS_Assist', '0003_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='upvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('of_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to='BITS_Assist.questions')),
            ],
        ),
        migrations.CreateModel(
            name='downvote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('of_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downvotes', to='BITS_Assist.questions')),
            ],
        ),
    ]