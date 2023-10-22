from django.db import models

"""
Create model Command and model Person.
"""


class Command(models.Model):
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        """
        Magic method is redefined to show all information about Command.
        """
        return f"id: {self.pk}, name: {self.name}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Command object.
        """
        return f"Command(id={self.pk})"


class Person(models.Model):
    name = models.CharField(blank=False, max_length=50)
    surname = models.CharField(blank=False, max_length=50)
    mail = models.EmailField(blank=False, max_length=254)
    command = models.ForeignKey(Command, related_name='person', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Person.
        """
        return f"id: {self.pk},name: {self.name}, surname: {self.surname}, mail: {self.mail}, command: {self.command}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Person object.
        """
        return f"Person(id={self.pk})"
