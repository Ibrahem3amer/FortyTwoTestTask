import datetime
from django.core.exceptions import ValidationError
from hello.models import Person

class EditPersonValidator(object):
    """Validator for business logic of person model"""

    @classmethod
    def validate_birth_date(cls, birth_date):
        """
        Accepts birth_date and validates that it's older than 10 years from now.
        """
        bdate_to_list   = birth_date.split('-')
        now             = datetime.datetime.now()
        submitted_year  = bdate_to_list[2]
        
        if (now.year - int(submitted_year)) <= 10:
            return 0
        return 1





