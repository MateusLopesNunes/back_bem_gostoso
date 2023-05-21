from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon') #coloca os campos na tabela
    list_display_links = ('id', 'name') #vira links
    search_fields = ('name',) #cria uma pesquisa
    list_per_page = 10 #cria paginação

admin.site.register(Category, CategoryAdmin)
