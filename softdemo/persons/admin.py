from django.contrib import admin
from persons.models import Person, RecyclePerson

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(RecyclePerson)
class PersonAdmin(admin.ModelAdmin):

    actions = ['recover']
    
    def get_queryset(self, request):
        return RecyclePerson.deleted.filter(is_deleted=True)

    @admin.action(description="Recover Deleted Items")
    def recover(self, request, queryset):
        queryset.update(is_deleted = False, deleted_at = None)