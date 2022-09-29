from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('treats', 'treats')], max_length=60),
        ),
    ]