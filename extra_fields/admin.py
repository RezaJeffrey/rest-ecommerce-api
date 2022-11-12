from django.contrib import admin
from django import forms
from extra_fields.models import ExtraFieldValue, ExtraFieldName


class ValueInlineForm(forms.ModelForm):
    class Meta:
        model = ExtraFieldValue
        fields = [
            'product', 'field_name',
            'value', 'sku'
        ]


class ValueInline(admin.TabularInline):
    model = ExtraFieldValue
    form = ValueInlineForm
    extra = 3


class ExtraFieldAdmin(admin.ModelAdmin):
    inlines = [ValueInline]


admin.site.register(ExtraFieldName, ExtraFieldAdmin)




