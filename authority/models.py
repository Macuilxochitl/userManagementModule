from django.db import models
import random

# Create your models here.
class user(models.Model):
	id=models.AutoField("ID",primary_key=True)
	username=models.CharField(max_length=60,unique=True)
	password=models.CharField(max_length=257)
	createTime=models.DateTimeField(auto_now_add=True)
	lastUpdateTime=models.DateTimeField(auto_now=True)
	lastLoginTime=models.DateTimeField(auto_now=True)
	isAdmin=models.BooleanField(default=False)
	regIP=models.CharField(max_length=60,default="")
	isActivated=models.BooleanField(default=False)
	actCode=models.IntegerField(default=0)
	email=models.EmailField(max_length=100,default="")



	def __str__(self):
		return "email="+self.email+",username="+self.username+",password="+self.password+",createTime="+self.createTime.strftime('%y-%m-%d %H:%M:%S')+",lastLoginTime="+self.lastLoginTime.strftime('%y-%m-%d %H:%M:%S')+",ip="+self.regIP