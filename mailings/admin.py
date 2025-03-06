# coding=utf-8
from django.contrib import admin

from mailings.models import Message, Client


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'theme',
        'body',
        'owner',
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'date_of_birth',
        'comment',
        'creator',
    )
