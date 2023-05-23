from utils.enums import *
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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(
        max_length=255,
        choices=[(tag.value, tag.name) for tag in UserTypes],
        default=UserTypes.ADOPTER_FOSTER.value
    )
    care_preference = ArrayField(
        models.CharField(
        choices=[(tag.name, tag.value) for tag in CarePreferences], max_length=100),

    )
    preferred_species = ArrayField(
        models.CharField(choices=[(tag.name, tag.value) for tag in PetSpecies], max_length=100),
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
        max_length=100,
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
        max_length=100,
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

    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Dog(models.Model):
    organization_id = models.CharField(max_length=255) # need to make foreign key when 
    organization_animal_id = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    species = models.CharField(max_length=3, default='Dog')
    primary_breed = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in DogBreeds]
    )
    secondary_breed = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[(tag.value, tag.name) for tag in DogBreeds]
    )
    mixed_breed = models.BooleanField(default=False)
    unknown_breed = models.BooleanField(default=False)
    primary_color = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in DogColors]
    )
    secondary_color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[(tag.value, tag.name) for tag in DogColors]
    )
    tertiary_color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[(tag.value, tag.name) for tag in DogColors]
    )
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in PetGender])
    size = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in PetSizes])
    coat = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in DogCoats])
    name = models.CharField(max_length=100)
    description = models.TextField()
    primary_photo_small = models.URLField()
    primary_photo_medium = models.URLField()
    primary_photo_large = models.URLField()
    primary_photo_full = models.URLField()
    small_photo_urls = ArrayField(
        models.URLField(),
        default=None,
        null=True,
        blank=True,
    )
    medium_photo_urls = ArrayField(
        models.URLField(),
        default=None,
        null=True,
        blank=True,
    )
    large_photo_urls = ArrayField(
        models.URLField(),
        default=None,
        null=True,
        blank=True,
    )
    full_photo_urls = ArrayField(
        models.URLField(),
        default=None,
        null=True,
        blank=True,
    )
    video_urls = ArrayField(
        models.URLField(),
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in PetStatuses])
    spayed_neutered = models.BooleanField()
    house_trained = models.BooleanField()
    declawed = models.BooleanField()
    special_needs = models.BooleanField(null=True)
    shots_current = models.BooleanField()
    good_with_children = models.BooleanField(null=True)
    good_with_dogs = models.BooleanField(null=True)
    good_with_cats = models.BooleanField(null=True)
    tags = ArrayField(
        models.CharField(max_length=50),
        null=True,
        blank=True,
    )
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, null=True)

    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    distance = models.FloatField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Cat(models.Model):
    organization_id = models.CharField(max_length=255) # need to make foreign key when 
    organization_animal_id = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    species = models.CharField(max_length=3, default='Cat')
    primary_breed = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in CatBreeds]
    )
    secondary_breed = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[(tag.value, tag.name) for tag in CatBreeds]
    )
    mixed_breed = models.BooleanField(default=False)
    unknown_breed = models.BooleanField(default=False)
    primary_color = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in CatColors]
    )
    secondary_color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[(tag.value, tag.name) for tag in CatColors]
    )
    tertiary_color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[(tag.value, tag.name) for tag in CatColors]
    )
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in PetGender])
    size = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in PetSizes])
    coat = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in CatCoats])
    name = models.CharField(max_length=100)
    description = models.TextField()
    primary_photo_small = models.URLField()
    primary_photo_medium = models.URLField()
    primary_photo_large = models.URLField()
    primary_photo_full = models.URLField()
    small_photo_urls = ArrayField(
        models.URLField(),
        default=None,
        null=True,
        blank=True,
    )
    medium_photo_urls = ArrayField(
        models.URLField(),
        default=None,
        null=True,
        blank=True,
    )
    large_photo_urls = ArrayField(
        models.URLField(),
        default=None,
        null=True,
        blank=True,
    )
    full_photo_urls = ArrayField(
        models.URLField(),
        default=None,
        null=True,
        blank=True,
    )
    video_urls = ArrayField(
        models.URLField(),
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=50, choices=[(tag.value, tag.name) for tag in PetStatuses])
    spayed_neutered = models.BooleanField()
    house_trained = models.BooleanField()
    declawed = models.BooleanField(null=True)
    special_needs = models.BooleanField(null=True)
    shots_current = models.BooleanField()
    good_with_children = models.BooleanField(null=True)
    good_with_dogs = models.BooleanField(null=True)
    good_with_cats = models.BooleanField(null=True)
    tags = ArrayField(
        models.CharField(max_length=50),
        null=True,
        blank=True,
    )
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20, null=True)

    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    distance = models.FloatField(blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    