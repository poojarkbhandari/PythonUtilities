from django.db import models

# Create your models here.

class User:
    def __init__(self, acc_no, name, password, balance):
        self.acc_no = acc_no
        self.name = name
        self.password = password
        self.balance = balance