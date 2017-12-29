from django.db 		import models
from django.utils 	import timezone
# Post is a Django Model, so Django knows that it should be saved in DB
class Post(models.Model):
	'''
	ForeignKey 		is a link to another model
					also needs on_delete argument
	CharField 		is for defining a text with limited chars
	TextField 		is for defining a text without limit of chars
	DateTimeField 	is for date & time
	'''
	author 			= models.ForeignKey('auth.user',
										on_delete = models.DO_NOTHING)
	title 			= models.CharField(max_length = 200)
	text			= models.TextField()
	created_date 	= models.DateTimeField(
									default = timezone.now)
	published_date	= models.DateTimeField( blank 	= True,
											null	= True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title