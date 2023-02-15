from django.contrib.auth.models import User
from django.db import models


class Schema(models.Model):
    COLUMN_SEPARATORS = (
        (",", "Comma"),
        (";", "Semicolon"),
        ("\t", "Tab"),
        ("|", "Pipe"),
        (":", "Colon"),
        (" ", "Space"),
        ("~", "Tilde"),
        ("/", "Forward slash"),
    )
    STRING_CHARACTERS = (
        ("'", "Single Quotes"),
        ('"', "Double Quotes"),
        ("`", "Backtick"),
        ("|", "Pipe"),
        ("#", "Hash"),
        ("@", "At"),
    )
    name = models.CharField(max_length=120)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="schemas"
    )
    column_separator = models.CharField(
        max_length=1, choices=COLUMN_SEPARATORS, default=","
    )
    string_character = models.CharField(
        max_length=1, choices=STRING_CHARACTERS, default="'"
    )

    def __str__(self) -> str:
        """The method returns the schema name."""
        return self.name


class Column(models.Model):
    DATA_TYPES = (
        ("full_name", "Full Name"),
        ("job", "Job"),
        ("email", "Email"),
        ("domain_name", "Domain Name"),
        ("phone_number", "Phone Number"),
        ("company_name", "Company Name"),
        ("text", "Text"),
        ("integer", "Integer"),
        ("address", "Address"),
        ("date", "Date"),
    )

    name = models.CharField(max_length=120)
    data_type = models.CharField(max_length=30, choices=DATA_TYPES)
    order = models.PositiveIntegerField()
    schema = models.ForeignKey(
        Schema, on_delete=models.CASCADE, related_name="columns"
    )
    sentence_count = models.PositiveIntegerField(blank=True, null=True)
    min_value = models.IntegerField(blank=True, null=True)
    max_value = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        """The method returns the name of the column."""
        return self.name
