from django.db import models
from django.utils.text import slugify


# ------------------------
# 1. SERVICES SECTION
# ------------------------
class Service(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    icon = models.ImageField(upload_to="services/icons/", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ------------------------
# 2. CASE STUDIES SECTION
# ------------------------
class CaseStudy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="case_studies/")
    slug = models.SlugField(unique=True, blank=True)

    button_text = models.CharField(max_length=50, default="Read More")
    button_url = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ------------------------
# 3. DOCTORS SECTION
# ------------------------
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    qualifications = models.TextField()

    experience_years = models.PositiveIntegerField(default=1)
    total_patients = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)

    image = models.ImageField(upload_to="doctors/")
    slug = models.SlugField(unique=True, blank=True)

    button_text = models.CharField(max_length=50, default="View Profile")
    button_url = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ------------------------
# 4. TESTIMONIAL SECTION
# ------------------------
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    quote = models.TextField()

    profile_pic = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
