from django.db import models

class User(models.Model):
	name= models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=15, blank=True)
	role = models.CharField(max_length=15)
	password = models.CharField(max_length=225)
	photo = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

	def __str__(self):
		return self.name

class Tenant(models.Model):
	users_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tenant_id', null=True, blank=True)
	name= models.CharField(max_length=100)
	delivery = models.BooleanField()
	status = models.BooleanField()
	photo = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
	
	def __str__(self):
		return self.name

class Price(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='price', null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    duration = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
    	return self.name


class Address(models.Model):
	as_address = models.CharField(max_length=50)
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	province = models.CharField(max_length=100)
	city = models.CharField(max_length=100) 
	keluarahan = models.CharField(max_length=100)
	status = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

	def __str__(self):
		return self.as_alamat

class Rate(models.Model):
	#tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='rate_tenant', null=True, blank=True)
	#user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rate_user', null=True, blank=True)
	#user_id = models.ManyToManyField(User)
	tenant_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tenant_id', null=True, blank=True)
	tenant_id = models.ManyToManyField(Tenant)
	count_rate = models.FloatField(null=True, blank=True, default=0.0)
	message = models.TextField(default="", editable=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
