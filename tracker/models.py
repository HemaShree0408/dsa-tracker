from django.db import models

# Create your models here.
# Topic model to categorize problems by their respective topics (e.g., Arrays, Linked Lists, Dynamic Programming, etc.).
class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Problem model to store information about each problem, including its topic, name, difficulty, leetcode link, logic notes, and whether it has been solved or needs revision.
class Problem(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    difficulty = models.CharField(max_length=20)

    leetcode_link = models.URLField()

    logic_notes = models.TextField()

    solved = models.BooleanField(default=False)

    need_revision = models.BooleanField(default=False)

    def __str__(self):
        return self.name