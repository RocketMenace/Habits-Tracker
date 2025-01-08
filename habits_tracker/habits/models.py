from django.contrib.auth import get_user_model
from django.db.models import Q, F
from django.db import models

# Create your models here.

User = get_user_model()
NULLABLE = {
    "blank": True,
    "null": True,
}


class BaseHabit(models.Model):
    """Abstract base model for habits."""

    class Frequency(models.TextChoices):
        DAILY = "ежедневно"
        WEEKLY = "еженедельно"

    place = models.CharField(max_length=200, verbose_name="место")
    action = models.TextField(verbose_name="действие")
    start_time = models.DateTimeField(verbose_name="время начала")
    end_time = models.DateTimeField(verbose_name="время окончания")
    public = models.BooleanField(verbose_name="публичность")
    is_enjoyable = models.BooleanField(verbose_name="признак приятности")
    frequency = models.CharField(
        max_length=12,
        choices=Frequency.choices,
        default=Frequency.DAILY,
        verbose_name="периодичность",
    )
    user = models.ForeignKey(
        User, verbose_name="пользователи", on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class RegularHabit(BaseHabit):
    """Model for regular habit."""

    related_habit = models.ForeignKey(
        "habits.RelatedHabit",
        **NULLABLE,
        related_name="regular_habit",
        verbose_name="желаемая привычка",
        on_delete=models.CASCADE,
    )

    award = models.TextField(verbose_name="вознаграждение", **NULLABLE)


    class Meta:
        verbose_name = "обычная привычка"
        verbose_name_plural = "обычные привычки"
        constraints = [
            models.CheckConstraint(
                name="regular_habit_start_time_before_end_time",
                check=Q(start_time__lt=F("end_time")),
            )
        ]

    def __str__(self):
        return f"{self.action} {self.frequency} {self.is_enjoyable=}"


class RelatedHabit(BaseHabit):
    """Model for desired habit to acquire"""

    class Meta:
        verbose_name = "желаемая привычка"
        verbose_name_plural = "желаемые привычки"
        constraints = [
            models.CheckConstraint(
                name="related_habit_start_time_before_end_time",
                check=Q(start_time__lt=F("end_time")),
            )
        ]

    def __str__(self):
        return f"{self.action}"
