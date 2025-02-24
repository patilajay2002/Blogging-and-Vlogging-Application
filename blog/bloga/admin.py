from django.contrib import admin
from bloga.models import Post,Commentm
# Register your models here.
class PostAdmin(admin.ModelAdmin):
 list_display=['title','slug','author','body','publish','created','updated'
                  ,'status']
 list_filter=('status',)
 search_fields=('title','body')
 raw_id_fields=('author',)
 date_hierarchy='publish'
 ordering=['status','publish']
 prepopulated_fields={'slug':('title',)}  

class CommentsAdmin(admin.ModelAdmin):
 list_display=('name','email','post','body',
                     'created','updated','active')
 list_filter=('active','created','updated')
 search_fields=('name','email','body')              
admin.site.register(Post,PostAdmin)
admin.site.register(Commentm,CommentsAdmin)