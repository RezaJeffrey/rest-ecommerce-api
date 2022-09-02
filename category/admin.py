from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from category.models import Category


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_desplay=(
        'tree_actions',
        'indented_title',
    ),
    list_desplay_links=(
        'indented_title',
    ),
)


