from django.contrib import admin

# Register your models here.
from .models import Post, Comment, SiteImage, SiteLink, Paragraph, MyVideo

class MyVideoInline(admin.TabularInline):
	model = MyVideo
	extra = 1

class ParagraphInline(admin.StackedInline):
	model = Paragraph
	extra = 1
	inlines = [MyVideoInline, ]

class SiteLinkInline(admin.StackedInline):
	model = SiteLink
	extra = 1


class PostAdmin(admin.ModelAdmin):
	"""
	fieldsets = [
		('Post Title', {'fields':[post_title]}),
		('Post Main Image', {'fields':[post_main_image]}),
		('Published', {'fields':[pub_date]}),
	]
	"""
	inlines = [ParagraphInline, SiteLinkInline, ]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(SiteImage)
#admin.site.register(SiteLink)
#admin.site.register(Paragraph)
