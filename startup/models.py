from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .Manager import UserManager
from django.utils.translation import gettext_lazy as _
from datetime import datetime


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    UserId = models.AutoField(primary_key=True)
    name = models.CharField(_('Name'),max_length=50, validators=[
        MinLengthValidator(2, "The first name must be longer than 2 characters")
    ])
    email = models.EmailField(_('Email'),null=False)
    gender = models.CharField(_('Gender'),max_length=15, null=False)
    mobile = models.CharField(_('Mobile'),max_length=13, null=False)
    userName = models.CharField(_('UserName'),max_length=50, null=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = ['Name', 'mobile', 'gender', 'password', 'userName']

    objects = UserManager()

    def __str__(self):
        return self.userName


class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(_('Company Name'),max_length=50, null=False)
    speciality = models.CharField(_('Specialization'),max_length=50, null=False)
    productName = models.CharField(_('Product Name'),max_length=50, null=False)
    websiteUrl = models.URLField(_('Website URL'))
    userId = models.ForeignKey(to='startup.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.companyName


def msgMediaPath(senderId, receiverId):
    return f"Messages/{senderId}_{receiverId}/{datetime.now().strftime('%Y/%m/%d/%H/%M/%S')}"


class Messages(models.Model):
    msgId = models.AutoField(primary_key=True)
    content = models.CharField(_('Content'),max_length=100, null=False)
    senderId = models.ForeignKey(to='startup.User', related_name='MsgSender', on_delete=models.CASCADE)
    receiverId = models.ForeignKey(to='startup.User', related_name='MsgReceiver', on_delete=models.CASCADE)
    media = models.FileField(_('Media'),upload_to=msgMediaPath(senderId, receiverId))
    createDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.msgId


def feedMediaPath(senderId):
    return f"Feed/{senderId}/{datetime.now().strftime('%Y/%m/%d/%H/%M/%S')}"


class FeedPost(models.Model):
    feedId = models.AutoField(primary_key=True)
    senderId = models.ForeignKey(to='startup.User', on_delete=models.CASCADE, blank=False)
    heading = models.CharField(_('Heading'),max_length=30, null=False,blank=False)
    description = models.TextField(_('Description'), blank=False)
    websiteUrl = models.URLField(_('Website URL'),blank=True)
    media = models.ImageField(_('Image'),upload_to=feedMediaPath(senderId),blank=True)
    createDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.heading
