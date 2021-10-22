from django.contrib import admin
from .models import *
# Register your models here.

class c1ModelAdmin(admin.ModelAdmin):
	list_display=['que','op1','op2','op3','op4','ans']

class c2ModelAdmin(admin.ModelAdmin):
	list_display=['que','op1','op2','op3','op4','ans']


class b1ModelAdmin(admin.ModelAdmin):
	list_display=['que','op1','op2','op3','op4','ans']
class b2ModelAdmin(admin.ModelAdmin):
	list_display=['que','op1','op2','op3','op4','ans']


class m1ModelAdmin(admin.ModelAdmin):
	list_display=['que','op1','op2','op3','op4','ans']
class m2ModelAdmin(admin.ModelAdmin):
	list_display=['que','op1','op2','op3','op4','ans']

class p1ModelAdmin(admin.ModelAdmin):
	list_display=['que','op1','op2','op3','op4','ans']
class p2ModelAdmin(admin.ModelAdmin):
	list_display=['que','op1','op2','op3','op4','ans']

admin.site.register(c1Model, c1ModelAdmin)
admin.site.register(c2Model, c2ModelAdmin)
admin.site.register(p1Model, p1ModelAdmin)
admin.site.register(p2Model, p2ModelAdmin)
admin.site.register(m1Model, m1ModelAdmin)
admin.site.register(m2Model, m2ModelAdmin)
admin.site.register(b1Model, b1ModelAdmin)
admin.site.register(b2Model, b2ModelAdmin)