from django.contrib import admin
from .models import book
from .models import BorrowRecord
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile
from django.contrib.auth.models import User

@admin.register(book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', )
    search_fields = ('title', 'author', 'isbn')
    list_filter = ( 'published_date',)


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('user__username', 'book__title')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')
    search_fields = ('user__username', 'user__email')

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Unregister the original User admin and register the customised one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Also register Profile for direct access/managing
admin.site.register(Profile, ProfileAdmin)