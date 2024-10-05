from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from authentication.models import User

from django.conf import settings

class Registration(models.Model):
    # profile_ID = models.CharField(max_length=10)

    # baseId
    # user_id = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE,primary_key=True)
    # PersonalInformation
    # profile_username = models.CharField(max_length=120)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    time_of_birth = models.TimeField()
    place_of_birth = models.CharField(max_length=100)
    mother_tongue = models.CharField(max_length=50)
    marital_status = models.CharField(max_length=20)

    # FamilInformation
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    no_of_brothers = models.PositiveIntegerField()
    no_of_married_brothers = models.PositiveIntegerField()
    no_of_sisters = models.PositiveIntegerField()
    no_of_married_sisters = models.PositiveIntegerField()

    # PhysicalInformation
    height = models.FloatField()
    weight = models.FloatField()
    physical_status = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50)
    complexion = models.CharField(max_length=50)
    diet = models.CharField(max_length=50)
    # Education & Job
    educational_qualification = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    place_of_job = models.CharField(max_length=100)
    income_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    # Religious & Caste
    religious = models.CharField(max_length=100)
    caste = models.CharField(max_length=100)
    gothra = models.CharField(max_length=100)

    # Astro & Zodiac
    lagnam = models.CharField(max_length=100)
    raasi = models.CharField(max_length=100)
    star = models.CharField(max_length=100)
    dosha = models.CharField(max_length=100)
    # raasi_chart = models.ImageField(upload_to="raasi_chart/", height_field="150",width_field="150")
    raasi_chart = models.ImageField(upload_to="raasi_chart/",blank=True,null=True)
    navamsam_chart = models.ImageField(upload_to="navamsam_chart/",blank=True,null=True) #Image fields

    # Contact
    contact_name = models.CharField(max_length=120)
    mobileNumber = models.CharField(max_length=120)
    # mobileNumber = PhoneNumberField(null=True,blank=True)
    whatsapp = models.CharField(max_length=20)
    # whatsapp = PhoneNumberField(null=True,blank=True)
    country = models.CharField(default="india",max_length=120)
    state = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    # Photo 
    photo1 = models.ImageField(upload_to='photos/',blank=True,null=True)
    # photo1 = models.ImageField(upload_to=upload_to,blank=True,null=True)
    photo2 = models.ImageField(upload_to='photos/',blank=True,null=True)
    photo3 = models.ImageField(upload_to='photos/',blank=True,null=True)
    photo4 = models.ImageField(upload_to='photos/',blank=True,null=True)


    # Preference
    preference_religion = models.CharField(max_length=100)
    preference_caste = models.CharField(max_length=100)
    preference_marital_status = models.CharField(max_length=20)
    preference_diet = models.CharField(max_length=50)
    preference_educational_qualification = models.CharField(max_length=100)
    preference_job = models.CharField(max_length=100)
    preference_income_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    preference_location = models.CharField(max_length=120)
    #
    def __str__(self):
        return f" {self.user_id.username} {self.user_id} - {self.contact_name}"
    

def upload_to(instance, filename):
    return 'images/%s/%s' % (instance.user.user.username, filename)