from django.db import models


# Create your models here.【每个类的名字后面会自动加个s，然后再网页上显示出来】
class Topic(models.Model):
	"""用户使用的主题"""
	text = models.CharField(max_length=200)
	date_add = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text


class Entry(models.Model):
	"""学习的有关某个主题的具体知识"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Mate:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""返回模型的字符串表示"""
		return f"{self.text[:50]}"


class Climb(models.Model):
	"""学习的有关某个主题的具体知识"""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Mate:
		verbose_name_plural = 'climbs'

	def __str__(self):
		"""返回模型的字符串表示"""
		return f"{self.text[:20]}"
