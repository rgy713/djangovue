from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from markdown import Markdown

class Message(models.Model):
    recipient = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
        related_name='recipient_messages'
    )
    sender = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
        related_name='sender_messages'
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        return md_body, md.toc
