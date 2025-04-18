from django.contrib import admin
from .models import Student

# Register your models here.

# admin.site.register(Student)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin): # <- Customizing the admin display itself
    list_display = ('name', 'age', 'class_name', 'marks')
    list_filter = ('class_name',)
    ordering = ('name',)



'''

Option | Description | Example
list_display | Fields to show in the list view | list_display = ('name', 'age', 'class_name')
list_filter | Adds sidebar filters | list_filter = ('class_name', 'age')
search_fields | Adds a search box | search_fields = ('name',)
ordering | Default ordering of objects | ordering = ('name',)
list_editable | Make fields editable in list view | list_editable = ('age',)
readonly_fields | Make fields read-only | readonly_fields = ('created_at',)
fields | Controls the order and visibility of fields in the form | fields = ('name', 'age')
exclude | Fields to exclude from the form | exclude = ('internal_notes',)
fieldsets | Group fields into sections | See example below
inlines | Embed related models (e.g., ForeignKey) | See below
prepopulated_fields | Auto-fill fields (e.g., slugs) | prepopulated_fields = {'slug': ('name',)}
date_hierarchy | Adds date-based drill-down navigation | date_hierarchy = 'created_at'
save_on_top | Puts save buttons on top of form | save_on_top = True
empty_value_display | Custom display for empty values | empty_value_display = 'Not Available'

'''