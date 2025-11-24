from django.contrib import admin
from .models import Service, CaseStudy, Doctor, Testimonial, Banners, ContactRequest

prepopulated_fields = {'slug': ('name',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','slug','is_active','created_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ('title','slug','is_active','created_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','specialization','experience_years','rating','created_at','is_active')
    search_fields = ('name','specialization', 'experience_years')
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','is_active' )
    search_fields = ('name',)
    
@admin.register(Banners)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('img', 'is_desktop','is_active', 'created_at' )
    
@admin.register(ContactRequest)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone' ,'email')
    search_fields = ('first_name','last_name','phone' ,'email')
    
