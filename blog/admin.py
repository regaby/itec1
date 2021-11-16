from django.contrib import admin
from .models import Post, Autor, Modalidad, Categoria

class PostAdmin(admin.ModelAdmin):
    list_filter = ('autor', 'categorias', 'fecha')
    list_display = ('titulo', 'fecha', 'autor')
    prepopulated_fields = {'slug': ('titulo',)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Autor)
admin.site.register(Modalidad)
admin.site.register(Categoria)