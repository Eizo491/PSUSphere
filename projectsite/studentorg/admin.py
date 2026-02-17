from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "updated_at")
    search_fields = ("college_name",)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college", "updated_at")
    search_fields = ("prog_name", "college__college_name")
    list_filter = ("college",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "program", "updated_at")
    search_fields = ("lastname", "firstname", "student_id")
    list_filter = ("program",)