from .models import RelatedHabit, RegularHabit


def create_related_habit(
    *,
    place: str,
    action: str,
    start_time,
    end_time,
    public: bool,
) -> RelatedHabit:
    """Function for creating related habit model instance."""

    related_habit = RelatedHabit.objects.create(
        place=place, action=action, start_time=start_time, end_time=end_time, public=public
    )
    return related_habit


def create_regular_habit(
    user,
    *,
    place: str,
    action: str,
    start_time,
    end_time,
    public: bool,
    award: str,
    related_habit=None,
    frequency: str,
    is_enjoyable: bool,
) -> RegularHabit:
    """Function for creating regular habit model instance."""
    if related_habit:
        regular_habit = RegularHabit.objects.create(
            user,
            place=place,
            action=action,
            start_time=start_time,
            end_time=end_time,
            public=public,
            award=award,
            related_habit=related_habit,
            frequency=frequency,
            is_enjoyable=is_enjoyable,
        )
        return regular_habit
    else:
        regular_habit = RegularHabit.objects.create(
            user,
            place=place,
            action=place,
            start_time=start_time,
            end_time=end_time,
            public=public,
            award=award,
            frequency=frequency,
            is_enjoyable=is_enjoyable,
        )
        return regular_habit
