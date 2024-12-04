from datetime import datetime, timedelta

import factory
from django.utils import timezone
from faker import Faker

from habits_tracker.habits.models import RelatedHabit, RegularHabit
from habits_tracker.users.models import User

faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    email = factory.LazyAttribute(lambda _: faker.email())
    password = factory.LazyAttribute(lambda _: faker.password())


class AbstractHabitFactory(factory.django.DjangoModelFactory):

    class Meta:
        abstract = True

    place = factory.LazyAttribute(lambda _: faker.text(max_nb_chars=10))
    action = factory.LazyAttribute(lambda _: faker.text())
    start_time = factory.LazyAttribute(
        lambda _: faker.date_time_between_dates(
            datetime_start=datetime.now(tz=timezone.utc),
            datetime_end=datetime.now(tz=timezone.utc) + timedelta(days=7),
        )
    )
    end_time = factory.LazyAttribute(
        lambda self: self.start_time + timedelta(minutes=2)
    )
    public = factory.LazyAttribute(lambda _: faker.boolean(chance_of_getting_true=50))
    is_enjoyable = factory.LazyAttribute(
        lambda _: faker.boolean(chance_of_getting_true=50)
    )
    frequency = factory.LazyAttribute(
        lambda _: faker.random_element(["еженедельно", "ежедневно"])
    )


class RelatedHabitFactory(AbstractHabitFactory):

    class Meta:
        model = RelatedHabit

    is_enjoyable = True


class RegularHabitFactory(AbstractHabitFactory):

    class Meta:
        model = RegularHabit

    user = factory.SubFactory(UserFactory)
    related_habit = factory.SubFactory(RelatedHabitFactory)

    is_enjoyable = False


class RegularHabitWithAwardFactory(AbstractHabitFactory):

    class Meta:
        model = RegularHabit

    related_habit = factory.SubFactory(RelatedHabitFactory)

    award = factory.LazyAttribute(lambda _: faker.text())


class EnjoyableRegularHabitFactory(AbstractHabitFactory):

    class Meta:
        model = RegularHabit

    is_enjoyable = True
