import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvproject.settings')
django.setup()
from faker import Faker
f=Faker()
from myApp.models import Employee
def populate(n):
    for i in range(n):
        fno=f.random_int(min=1,max=20)
        fname=f.name()
        fsal=f.random_int(min=5000,max=100000)
        faddr=f.address()
        e=Employee.objects.get_or_create(eno=fno,ename=fname,esal=fsal,eaddr=faddr)
populate(25)
