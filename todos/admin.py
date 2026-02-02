from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'is_completed', 'due_date', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'due_date', 'created_at')
    search_fields = ('title', 'description', 'owner__username', 'owner__email')
    ordering = ('-created_at',)
    autocomplete_fields = ('owner',)
