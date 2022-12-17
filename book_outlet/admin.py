from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
  #  readonly_fields = ("slug",) # to make a coulumn read only and not editable in the admin form
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",) # makng a filter on the right of the page to filter the date by the values of each column
    list_display = ("title", "author",) # which columns to display 

admin.site.register(Book, BookAdmin)