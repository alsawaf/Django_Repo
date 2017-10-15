import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Project1_Practice.settings')

import django
django.setup()

from app1.models import user
from faker import Faker

fake_generator = Faker()

def populate(N=10):


     for entry in range (N=5):

         Fake_Name = fake_generator.name().split()
         Fake_First_Name = Fake_Name[0]
         Fake_Last_Name = Fake_Name[1]
         Fake_Email = fake_generator.email()

         user = user.objects.get_or_create(First_Name = Fake_First_Name ,
                                           Last_Name = Fake_Last_Name , Email = Fake_Email)[0]


     if __name__ == '__main__':
         print("Filling DataBase")
         populate(20)
         print("Done !")

