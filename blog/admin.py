from django.contrib import admin
from.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Meta:
        fields="__all__"

