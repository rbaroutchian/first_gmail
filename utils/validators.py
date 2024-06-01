from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if not value.isdigit() or len(value) not in range(10, 16):
        raise ValidationError(_('Phone number must be numeric and between 10 to 15 digits.'), params={'value': value},)
