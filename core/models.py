from utils.enums import UserTypes, CarePreferences, PetSpecies, PetTemperaments, DogBreeds, DogCharacteristics, CatBreeds, CatCharacteristics
from enumfields import EnumField
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db.models import Q
from django.db import models


def validate_age(value):
    if isinstance(value, int):
        if value <= 0:
            raise ValidationError("Age must be greater than 0")
    elif isinstance(value, list) and len(value) == 2:
        if value[0] <= 0 or value[1] <= 0 or value[0] >= value[1]:
            raise ValidationError("Age range must be greater than 0 and in ascending order")
    elif not isinstance(value, None):
        raise ValidationError("Age must be an integer or a list of two integers")


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255, default='TEMP')
    last_name = models.CharField(max_length=255, default='TEMP')
    email = models.EmailField(max_length=255, default='TEMP', unique=True)
    phone = models.CharField(max_length=255, default='TEMP', unique=True)
    user_type = models.CharField(
        max_length=255,
        choices=[(tag.value, tag.name) for tag in UserTypes],
        default=UserTypes.ADOPTER_FOSTER.value
    )
    care_preference = ArrayField(
        models.CharField(
        choices=[(tag.name, tag.value) for tag in CarePreferences], max_length=100),
        default=[CarePreferences.ADOPTING.value,  CarePreferences.FOSTERING.value],
    )
    preferred_species = ArrayField(
        models.CharField(choices=[(tag.name, tag.value) for tag in PetSpecies], max_length=100),
        default=[PetSpecies.DOG.value, PetSpecies.CAT.value],
    )

    # Dog preferences
    preferred_dog_age = ArrayField(
        models.PositiveIntegerField(validators=[validate_age]), 
        size=2,
        default=None,
        null=True,
        blank=True,
    )
    preferred_dog_breeds = ArrayField(
        models.CharField(choices=[(tag.name, tag.value) for tag in DogBreeds], max_length=100),
        default=None,
        null=True,
        blank=True,
    )
    preferred_dog_characteristics = ArrayField(
        models.CharField(choices=[(tag.name, tag.value) for tag in DogCharacteristics], max_length=100),
        default=None,
        null=True,
        blank=True,
    )
    preferred_dog_temperaments = ArrayField(
        models.CharField(choices=[(tag.name, tag.value) for tag in PetTemperaments], max_length=100),
        default=None,
        null=True,
        blank=True,
    )

    # Cat preferences
    preferred_cat_age = ArrayField(
        models.PositiveIntegerField(validators=[validate_age]), 
        size=2,
        default=None,
        null=True,
        blank=True,
    )
    preferred_cat_breeds = ArrayField(
        models.CharField(choices=[(tag.name, tag.value) for tag in CatBreeds], max_length=100),
        default=None,
        null=True,
        blank=True,
    )
    preferred_cat_characteristics = ArrayField(
        models.CharField(choices=[(tag.name, tag.value) for tag in CatCharacteristics], max_length=100),
        default=None,
        null=True,
        blank=True,
    )
    preferred_cat_temperaments = ArrayField(
        models.CharField(choices=[(tag.name, tag.value) for tag in PetTemperaments], max_length=100),
        default=None,
        null=True,
        blank=True,
    )

    address1 = models.CharField(max_length=255, default='TEMP')
    address2 = models.CharField(max_length=255, default='TEMP')
    city = models.CharField(max_length=255, default='TEMP')
    state = models.CharField(max_length=255, default='TEMP')
    zip = models.PositiveIntegerField(default=0)