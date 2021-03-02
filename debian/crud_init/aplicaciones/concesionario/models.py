from enum import Enum
from django.db import models


# Models for my usuars
class User(models.Model):
    """
    Users Class model
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=25)

    def __str__(self):
        return str(self.id) + " " + str(self.username) + " " + str(self.email) + " " + str(self.password)


class Car(models.Model):
    """
    Car Class model
    """

    class DOORS(Enum):
        """
        Class for choice field
        resource = https://www.merixstudio.com/blog/django-models-declaring-list-available-choices-right-way/
        """
        one = ('1', '1')
        two = ('2', '2')
        three = ('3', '3')
        four = ('4', '4')
        six = ('6', '5')

        # Atribute Getter
        @classmethod
        def get_value(cls, member):
            return member.value[0]

    class COLORS(Enum):
        """
        Class for Possible colors
        """
        black = ('black', 'black')
        blue = ('blue', 'blue')
        white = ('white', 'white')
        red = ('red', 'red')
        grey = ('grey', 'grey')
        yellow = ('yellow', 'yellow')

        # Atribute Getter
        @classmethod
        def get_value(cls, member):
            return member.value[0]

    id = models.AutoField(primary_key=True)
    matr = models.CharField(max_length=7).unique
    price = models.DecimalField(default=10000, max_digits=7, decimal_places=2)  # max value
    marc = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    n_doors = models.CharField(
        max_length=32,
        choices=[x.value for x in DOORS],  # Doors loop as choices
        default=DOORS.get_value(DOORS.four),  # Default
    )
    colors = models.CharField(
        max_length=32,
        # ITS MUST BE A TUPLE
        choices=[x.value for x in COLORS],  # Doors loop as choices
        default=COLORS.get_value(COLORS.black),  # Default
    )
    age = models.DateField()

    def __str__(self):
        return str(self.id) + " " + str(self.matr) + " " + str(self.price) + " " + str(self.marc) + " " + str(
            self.model) \
               + " " + str(self.n_doors) + " " + str(self.colors) + " " + str(self.age)


