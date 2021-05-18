# Generated by Django 3.2.2 on 2021-05-18 23:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Election",
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
                (
                    "election_name",
                    models.CharField(
                        help_text="Name your election (i.e., 4th Year Chair).",
                        max_length=80,
                    ),
                ),
                (
                    "seats_available",
                    models.IntegerField(
                        help_text="How many seats are there in this election?",
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, message="There must be at least one position open"
                            )
                        ],
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("referenda", "Referenda"),
                            ("officer", "Officer"),
                            ("board_of_directors", "Board of Directors"),
                            ("discipline_club", "Discipline Clubs"),
                            ("class_representative", "Class Representatives"),
                            ("other", "Other"),
                        ],
                        help_text="What category does this election belong to?",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ElectionSession",
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
                (
                    "election_session_name",
                    models.CharField(
                        help_text="Name your Election Session (i.e., Fall 2021).",
                        max_length=50,
                    ),
                ),
                (
                    "start_time",
                    models.DateTimeField(
                        help_text="When does your Election Session start?"
                    ),
                ),
                (
                    "end_time",
                    models.DateTimeField(
                        help_text="When does your Election Session finish?"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Election Sessions",
            },
        ),
        migrations.CreateModel(
            name="Voter",
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
                ("student_number_hash", models.CharField(max_length=16)),
                (
                    "discipline",
                    models.CharField(
                        choices=[
                            ("ENG", "Track One Engineering"),
                            ("CHE", "Chemical Engineering"),
                            ("CIV", "Civil Engineering"),
                            ("ELE", "Electrical Engineering"),
                            ("CPE", "Computer Engineering"),
                            ("ESC", "Engineering Science"),
                            ("IND", "Industrial Engineering"),
                            ("LME", "Mineral Engineering"),
                            ("MEC", "Mechanical Engineering"),
                            ("MMS", "Materials Science Engineering"),
                        ],
                        max_length=45,
                    ),
                ),
                ("engineering_student", models.BooleanField()),
                (
                    "study_year",
                    models.IntegerField(
                        choices=[
                            (1, "First Year"),
                            (2, "Second Year"),
                            (3, "Third Year"),
                            (4, "Fourth Year"),
                        ]
                    ),
                ),
                ("pey", models.BooleanField()),
                (
                    "student_status",
                    models.CharField(
                        choices=[
                            ("full_time", "Full Time"),
                            ("part_time", "Part Time"),
                        ],
                        max_length=20,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                (
                    "message",
                    models.TextField(
                        help_text="This message will be displayed overhead the website."
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True,
                        help_text="Check to make alert active. Active alerts will appear on the website, inactive ones will not.",
                    ),
                ),
                (
                    "hideable",
                    models.BooleanField(
                        default=False,
                        help_text="Check to allow user to hide the alert on the website. Unchecked alerts will be persistent",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "election_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="backend.electionsession",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Eligibility",
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
                (
                    "eng_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Track One Engineering Eligible?"
                    ),
                ),
                (
                    "che_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Chemical Engineering Eligible?"
                    ),
                ),
                (
                    "civ_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Civil Engineering Eligible?"
                    ),
                ),
                (
                    "ele_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Electrical Engineering Eligible?"
                    ),
                ),
                (
                    "cpe_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Computer Engineering Eligible?"
                    ),
                ),
                (
                    "esc_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Engineering Science Eligible?"
                    ),
                ),
                (
                    "ind_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Industrial Engineering Eligible?"
                    ),
                ),
                (
                    "lme_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Mineral Engineering Eligible?"
                    ),
                ),
                (
                    "mec_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Mechanical Engineering Eligible?"
                    ),
                ),
                (
                    "mms_eligible",
                    models.BooleanField(
                        default=False,
                        verbose_name="Materials Science Engineering Eligible?",
                    ),
                ),
                (
                    "year_1_eligible",
                    models.BooleanField(
                        default=False, verbose_name="First Years Eligible?"
                    ),
                ),
                (
                    "year_2_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Second Years Eligible?"
                    ),
                ),
                (
                    "year_3_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Third Years Eligible?"
                    ),
                ),
                (
                    "year_4_eligible",
                    models.BooleanField(
                        default=False, verbose_name="Fourth Years Eligible?"
                    ),
                ),
                (
                    "pey_eligible",
                    models.BooleanField(
                        default=False, verbose_name="PEY Students Eligible?"
                    ),
                ),
                (
                    "status_eligible",
                    models.CharField(
                        choices=[
                            ("full_time", "Full Time"),
                            ("part_time", "Part Time"),
                            ("full_and_part_time", "Full and Part Time"),
                        ],
                        help_text="Student statuses eligible",
                        max_length=30,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "election",
                    models.OneToOneField(
                        help_text="Which election do you want to define eligibility for?",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eligibilities",
                        to="backend.election",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Eligibilities",
            },
        ),
        migrations.AddField(
            model_name="election",
            name="election_session",
            field=models.ForeignKey(
                help_text="Which Election Session does this election belong in?",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="elections",
                to="backend.electionsession",
            ),
        ),
        migrations.CreateModel(
            name="Candidate",
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
                (
                    "candidate_name",
                    models.CharField(
                        help_text="What is the name of the Candidate?", max_length=100
                    ),
                ),
                (
                    "statement",
                    models.TextField(
                        blank=True,
                        help_text="Enter Candidate or Referendum statement.",
                        null=True,
                    ),
                ),
                (
                    "disqualified_status",
                    models.BooleanField(
                        default=False,
                        help_text="Has the Candidate been disqualified? (Default is False)",
                    ),
                ),
                (
                    "disqualified_link",
                    models.URLField(
                        blank=True,
                        help_text="(Optional) Enter a link to the disqualification ruling.",
                        null=True,
                    ),
                ),
                (
                    "disqualified_message",
                    models.TextField(
                        blank=True,
                        help_text="(Optional) Enter a disqualification ruling message for this Candidate.",
                        null=True,
                    ),
                ),
                (
                    "rule_violation_message",
                    models.TextField(
                        blank=True,
                        help_text="(Optional) Enter a rule violation message for this Candidate.",
                        null=True,
                    ),
                ),
                (
                    "rule_violation_link",
                    models.URLField(
                        blank=True,
                        help_text="(Optional) Enter a link to the rule violation ruling.",
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "election",
                    models.ForeignKey(
                        help_text="Which Election is this Candidate running in?",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="candidates",
                        to="backend.election",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ballot",
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
                ("rank", models.IntegerField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "candidate",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ballots",
                        to="backend.candidate",
                    ),
                ),
                (
                    "election",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ballots",
                        to="backend.election",
                    ),
                ),
                (
                    "voter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ballots",
                        to="backend.voter",
                    ),
                ),
            ],
        ),
    ]
