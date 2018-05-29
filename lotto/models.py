from django.db import models
from django.utils import timezone

import random

# Create your models here.

class GuessNumber(models.Model):
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=255)
    lottos = models.CharField(max_length=255,
                              default='[1,2,3,4,5,6]')
    num_lotto = models.CharField(max_length=1)
    update_date = models.DateTimeField()

    def generate(self):
        self.lottos = ''
        origin = list(range(1,46))
        for _ in range(0,int(self.num_lotto)):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos +=  str(guess) + '\n'
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s %s" %(self.name, self.text)