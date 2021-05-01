from django.contrib import admin
from .models import Employees, Departments, DeptEmp, DeptManager, Salaries, Titles
# Register your models here.
admin.site.register(Employees)
admin.site.register(Departments)
admin.site.register(DeptEmp)
admin.site.register(DeptManager)
admin.site.register(Salaries)
admin.site.register(Titles)

admin.site.site_header = "Ingenieria Inversa"
admin.site.site_title = "CRUD"
admin.site.index_title = "Bienvenidos al portal de administración"