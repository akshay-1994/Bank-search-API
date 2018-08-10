# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from fyleRestApi.models import IndianBanks

# Register your models here.


class IndianBanksAdmin(admin.ModelAdmin):
    pass
admin.site.register(IndianBanks)
