# Generated by Django 5.1.1 on 2024-11-30 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("babyaccountsapp", "0002_customer_remove_accountingentry_business_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Business",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Ledger",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "ledger_head",
                    models.CharField(
                        choices=[
                            ("direct_income", "Direct Income"),
                            ("direct_expense", "Direct Expense"),
                            ("credit_sales", "Credit Sales"),
                            ("received_sales", "Received Sales"),
                            ("loan_received", "Loan Received"),
                            ("loan_paid", "Loan Paid"),
                            ("transfer_service", "Transfer Service"),
                            ("other_service", "Other Service"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="amount",
        ),
        migrations.AddField(
            model_name="transaction",
            name="cr",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="transaction",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="transaction",
            name="dr",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="transaction",
            name="gst",
            field=models.CharField(
                choices=[("with_gst", "With GST"), ("without_gst", "Without GST")],
                default="with_gst",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="business",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="babyaccountsapp.business",
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="ledger",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="babyaccountsapp.ledger",
            ),
        ),
        migrations.AddField(
            model_name="ledger",
            name="mode",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="babyaccountsapp.mode"
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="mode",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="babyaccountsapp.mode",
            ),
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
    ]
