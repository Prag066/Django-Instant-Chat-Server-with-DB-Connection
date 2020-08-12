from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from .models import Person,Message,CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    empty_value_display = '-empty-'
    list_display = ('admin_image_url','username','email', 'is_staff',)
    list_filter = ('username','email', 'is_active',
        ('is_staff', admin.BooleanFieldListFilter),
        # ('email', admin.EmptyFieldListFilter),
    )
    list_display_links = ('username','admin_image_url',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Extra', {'fields': ('image',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)

    def admin_image_url(self,obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 45px; height:45px;" />')
        else:
            return "No image"
    


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Person)
admin.site.register(Message)