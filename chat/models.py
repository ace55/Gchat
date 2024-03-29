from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from psycopg2 import Timestamp

class PrivateChatRoom(models.Model):
    """
    A private room for people to chat in.
    """
    user1               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user1")
    user2               = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user2")

	# Users who are currently connected to the socket (Used to keep track of unread messages)
    connected_users     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="connected_users")
    is_active 			= models.BooleanField(default=True)

    def connect_user(self, user):
        """
        return true if user is added to the connected_users list
        """
        is_user_added = False
        if not user in self.connected_users.all():
            self.connected_users.add(user)
            is_user_added = True
        return is_user_added 


    def disconnect_user(self, user):
        """
        return true if user is removed from connected_users list
        """
        is_user_removed = False
        if user in self.connected_users.all():
            self.connected_users.remove(user)
            is_user_removed = True
        return is_user_removed

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to get sent
        messages as they are generated.
        """
        return f"PrivateChatRoom-{self.id}"


class RoomChatMessageManager(models.Manager):
	def by_room(self, room):
		qs = RoomChatMessage.objects.filter(room=room).order_by("-timestamp")
		return qs

class RoomChatMessage(models.Model):
	"""
	Chat message created by a user inside a Room
	"""
	user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	room                = models.ForeignKey(PrivateChatRoom, on_delete=models.CASCADE)
	timestamp           = models.DateTimeField(auto_now_add=True)
	content             = models.TextField(unique=False, blank=False,)

	objects = RoomChatMessageManager()


	def __str__(self):
		return self.content


