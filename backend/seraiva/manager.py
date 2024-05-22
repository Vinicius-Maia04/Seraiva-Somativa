from django.contrib.auth.models import BaseUserManager
import random

class CustomManager(BaseUserManager):

    def create_user(self, email, password=None, phoneNumber=None, **extra_fields):

        if not email:
            raise  ValueError("Invalid e-mail!")
        
        email = self.normalize_email(email)
   
        user = self.model(
            email=email,
            phoneNumber=phoneNumber,       
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_superuser(self, email, password=None, phoneNumber='19994893939', **extra_fields):
        #se é criação de super user, então seta estes atributos automaticamente:
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        return self.create_user(email, password, phoneNumber, **extra_fields)
            
        