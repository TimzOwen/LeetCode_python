# find the first recurring char in a given set of character.

def recurring_char(given_string):    
    char_list = {}
    for chars in given_string:
        if chars in char_list:
            return chars
        else:
            char_list[chars] = 1
    return None

print(recurring_char('DABCDBCD')) # returns 'D' being the first char and repetitive



#  Models
from django.core.exceptions import ValidationError
from django.db import models


class Customer(models.Model):
    # No need to update these
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    # TODO: HERE
    gender = models.CharField(max_length=100)
    email = models.EmailField()
    lat = models.IntegerField()
    
    lng = ???

    def clean(self):
        # Make sure both (lat, lng) are set or neither.
        coords = [self.lat, self.lng]
        if any(coords) and not all(coords):
            raise ValidationError("Cannot insert partial coordinates.")
        super().clean()  # no-op for models.Model inheritance.
