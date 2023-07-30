from django.contrib import admin


""" class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')  # Open in Django Admin (access /admin website section) and add in Blog list the real blog name and status (enabled/disabled): http://prntscr.com/nnsoa8 (ref: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
"""

from apps.blog.models import Blog, Category, Comments


admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comments) #add Comments access