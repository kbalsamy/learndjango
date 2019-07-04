from django.db import models

# Create your models here.
# learn recursive relationship


class Employee(models.Model):

    designation = [
        ('pres', 'President'),
        ('man', 'Manager'),
        ('sta', 'Staff')]

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    role = models.CharField(max_length=10, choices=designation, default='Staff')
    manager = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, related_name='employee')

    def __str__(self):

        return self.firstName + " " + self.lastName
