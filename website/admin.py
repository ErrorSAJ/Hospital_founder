from django.contrib import admin
from .models import Service, CaseStudy, Doctor, Testimonial

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
    
