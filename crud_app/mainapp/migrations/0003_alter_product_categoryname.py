# Generated by Django 5.1.1 on 2024-09-12 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0002_alter_product_categoryname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="categoryName",
            field=models.ForeignKey(
                choices=[
                    ("LP", "Laptop"),
                    ("MB", "Mobile"),
                    ("KC", "Kitchens"),
                    ("AC", "Accessories"),
                    ("HS", "Household"),
                ],
                max_length=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category",
                to="mainapp.productcategory",
            ),
        ),
    ]
