from django.contrib import admin
from .models import Post, Announcement, Comment
from django.contrib.auth.models import Group

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    #list_filter = ("status",)
    search_fields = ['title', 'content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin)
admin.site.register(Announcement)
admin.site.unregister(Group)
