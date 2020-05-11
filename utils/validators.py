import phonenumbers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.files.images import get_image_dimensions


def validate_mobile_number(value):
    """
    To use this function you need to install phonenumbers package

    https://github.com/daviddrysdale/python-phonenumbers


    Without any packages eg:

    phone_number = models.CharField(

        max_length= 16,

        validators=[

            RegexValidator(

                regex=r'^\+?1?\d{d,15}$',

                message='Phone number must be entered in the format '+123456789'.

            )

        ]

    )

    """
    if value.startswith(('+', '00', '0')):
        phone_number = phonenumbers.parse(value, None)
        if phonenumbers.is_possible_number(phone_number) and phonenumbers.is_valid_number(phone_number):
            return True
        else:
            raise ValidationError(
                _('Please enter valid phone numbers')
            )
    else:
        raise ValidationError(
            _('Please enter phone number with country code')
        )


def validate_image_dimension(value):
    """
    Need to tweak as requirements
    """
    w, h = get_image_dimensions(value)
    if w != 100:
        raise ValidationError("The image is %i pixel wide. It's supposed to be 100px" % w)
    if h != 200:
        raise ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)


def validate_file_size(value):
    """
    limit_mb = 8
    if file_size > limit_mb * 1024 * 1024:
    raise ValidationError("Max size of file is %s MB"II % limit_mb)
    """
    file_size = value.file.size
    limit_kb = 150
    if file_size > limit_kb * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_kb)
