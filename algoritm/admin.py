from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# admin.site.register(Boards)
# admin.site.register(Category)


class BoardsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{ object.photo.url }' width=50>")

    get_html_photo.short_description = 'preview'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Boards, BoardsAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.site_title = 'Админ панель сайта АМ2'
admin.site.site_header = 'Админ панель сайта АМ2'