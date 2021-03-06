# Generated by Django 2.0.3 on 2018-10-27 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreeTipsGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('home_team', models.CharField(max_length=200, null=True)),
                ('home_score', models.PositiveIntegerField(default=0)),
                ('away_score', models.PositiveIntegerField(default=0)),
                ('away_team', models.CharField(max_length=200, null=True)),
                ('prediction', models.CharField(max_length=100, null=True)),
                ('odds', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Won', 'Won'), ('Lost', 'Lost')], default='running', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=150, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='freetipsgame',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tips.Ticket'),
        ),
    ]
