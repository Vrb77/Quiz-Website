from django.db import models

# Create your models here.
class c1Model(models.Model):
	que=models.CharField(max_length=300,null=True)
	op1=models.CharField(max_length=300,null=True)
	op2=models.CharField(max_length=300,null=True)
	op3=models.CharField(max_length=300,null=True)
	op4=models.CharField(max_length=300,null=True)
	ans=models.CharField(max_length=300,null=True)
	
class c2Model(models.Model):
	que=models.CharField(max_length=300,null=True)
	op1=models.CharField(max_length=300,null=True)
	op2=models.CharField(max_length=300,null=True)
	op3=models.CharField(max_length=300,null=True)
	op4=models.CharField(max_length=300,null=True)
	ans=models.CharField(max_length=300,null=True)

class p1Model(models.Model):
	que=models.CharField(max_length=300,null=True)
	op1=models.CharField(max_length=300,null=True)
	op2=models.CharField(max_length=300,null=True)
	op3=models.CharField(max_length=300,null=True)
	op4=models.CharField(max_length=300,null=True)
	ans=models.CharField(max_length=300,null=True)

class p2Model(models.Model):
	que=models.CharField(max_length=300,null=True)
	op1=models.CharField(max_length=300,null=True)
	op2=models.CharField(max_length=300,null=True)
	op3=models.CharField(max_length=300,null=True)
	op4=models.CharField(max_length=300,null=True)
	ans=models.CharField(max_length=300,null=True)

class m1Model(models.Model):
	que=models.CharField(max_length=300,null=True)
	op1=models.CharField(max_length=300,null=True)
	op2=models.CharField(max_length=300,null=True)
	op3=models.CharField(max_length=300,null=True)
	op4=models.CharField(max_length=300,null=True)
	ans=models.CharField(max_length=300,null=True)

class m2Model(models.Model):
	que=models.CharField(max_length=300,null=True)
	op1=models.CharField(max_length=300,null=True)
	op2=models.CharField(max_length=300,null=True)
	op3=models.CharField(max_length=300,null=True)
	op4=models.CharField(max_length=300,null=True)
	ans=models.CharField(max_length=300,null=True)

class b1Model(models.Model):
	que=models.CharField(max_length=300,null=True)
	op1=models.CharField(max_length=300,null=True)
	op2=models.CharField(max_length=300,null=True)
	op3=models.CharField(max_length=300,null=True)
	op4=models.CharField(max_length=300,null=True)
	ans=models.CharField(max_length=300,null=True)

class b2Model(models.Model):
	que=models.CharField(max_length=300,null=True)
	op1=models.CharField(max_length=300,null=True)
	op2=models.CharField(max_length=300,null=True)
	op3=models.CharField(max_length=300,null=True)
	op4=models.CharField(max_length=300,null=True)
	ans=models.CharField(max_length=300,null=True)

class contact(models.Model):
	username=models.CharField(max_length=300)
	name=models.CharField(max_length=300)
	mail=models.CharField(max_length=300)
	subject=models.CharField(max_length=500)
	msg=models.CharField(max_length=300)


	



