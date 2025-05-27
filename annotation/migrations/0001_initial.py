import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('status', models.PositiveIntegerField(choices=[(1, 'Unannotated'), (2, 'Annotated'), (3, 'Finished Annotation')], default=1)),
                ('save_finished_annotation', models.BooleanField(default=False)),
                ('last_annotated_at', models.DateTimeField(auto_now_add=True)),
            name='Annotate',
            name="Annotation",
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
                ("text", models.TextField()),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Unannotated"),
                            (2, "Annotated"),
                            (3, "Finished Annotation"),
                        ],
                        default=1,
                    ),
                ),
                ("save_finished_annotation", models.BooleanField(default=False)),
                ("last_modified_at", models.DateTimeField(auto_now_add=True)),
                (
                    "annotated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "last_modified_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="last_modified_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
