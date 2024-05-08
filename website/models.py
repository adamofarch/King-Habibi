from django.db import models

class userData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name 
    
class submittedEmails(models.Model):
    submittedEmail = models.EmailField(max_length=50)

    def __str__(self):
        return self.submittedEmail
