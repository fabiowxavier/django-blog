from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField(default="No content")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"  

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)    
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.body} | written by {self.author}"  

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    ticket_holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_tickets"
    )
    date_issued = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )

    def __str__(self):
        return f"Ticket for {self.ticket_holder} to {self.event.name}"