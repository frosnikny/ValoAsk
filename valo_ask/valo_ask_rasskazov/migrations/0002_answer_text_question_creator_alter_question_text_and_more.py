from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('valo_ask_rasskazov', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='text',
            field=models.CharField(default='answer text', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='valo_ask_rasskazov.user'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(default='question text', max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=127, unique=True),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='is_good',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='is_question',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=31, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=31, unique=True),
        ),
    ]
