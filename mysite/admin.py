
from django.contrib import admin
from .models import Project, Comments, Profile
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'phone', 'address', 'created' )
    list_filter = ( 'created', 'author')
admin.site.register(Company,CompanyAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('company','title','author','created')
    list_filter = ('company', 'author','created')
admin.site.register(Project,ProjectAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('project', 'author', 'create_date', 'comment', 'status')
    list_filter = ('status', 'create_date')
    search_fields = ('project','comment')
admin.site.register(Comments, CommentAdmin)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email','avatar' ,'bio' , 'location' ,'birth_date']
admin.site.register(Profile, ProfileAdmin)


# Register your models here.
