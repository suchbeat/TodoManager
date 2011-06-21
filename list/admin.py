from django.contrib import admin
from TodoManager.list.models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'user', 'creation_date')
	search_fields = ('title', 'description')
	list_filter = ('creation_date',)
	fields = ('title', 'description', 'user', 'creation_date')

admin.site.register(Item, ItemAdmin)
