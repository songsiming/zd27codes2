from learning_logs.models import Topic

print(Topic.objects.all())

topics = Topic.objects.all()
for topic in topics:
	print(topic.id, topic)
