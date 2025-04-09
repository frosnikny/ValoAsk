from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valo_ask_rasskazov', '0002_answer_text_question_creator_alter_question_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='summary_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
