from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_none_zero(value):
    if value == 0:
        raise ValidationError(
            _('%(value) can\'t be zero!'),
            params={'value': value}
        )







