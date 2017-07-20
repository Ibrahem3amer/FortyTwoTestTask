import datetime


class EditPersonValidator(object):
    """Validator for business logic of person model"""

    @classmethod
    def validate_birth_date(cls, birth_date):
        """validates birth_date > 10 years from now."""
        bdate_to_list = birth_date.split('-')
        now = datetime.datetime.now()
        submitted_year = bdate_to_list[2]

        if (now.year - int(submitted_year)) <= 10:
            return 0
        return 1
