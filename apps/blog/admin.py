from django.contrib import admin

from .models import Blog, Category, Comment

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)

admin.site.register(Blog)
admin.site.register(Category)

# admin.site.register(Comment)
