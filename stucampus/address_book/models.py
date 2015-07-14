from django.db import models

# Create your models here.

class Member(models.Model):
	name=models.CharField(max_length=20)
	grade=models.CharField(max_length=20)
	sex=models.CharField(max_length=1)
	department=models.CharField(max_length=20,blank=True)
	position=models.CharField(max_length=20,blank=True)
	stuID=models.CharField(max_length=20,blank=True)
	dormitory=models.CharField(max_length=20,blank=True)
	birthday_type=models.CharField(max_length=20,blank=True)
	#birthday=models.DateField()
	phone_num_long=models.CharField(max_length=20,blank=True)
	phone_num_short=models.CharField(max_length=20,blank=True)
	is_work=models.CharField(max_length=3,blank=True)
	wechat=models.CharField(max_length=20,blank=True)
	qq=models.CharField(max_length=20,blank=True)
	
	def __unicode__(self):
		return self.name

class Manager(models.Model):
	managername = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.managername





	

