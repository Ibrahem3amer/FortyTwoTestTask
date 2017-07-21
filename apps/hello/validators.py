import datetime


class EditPersonValidator(object):
    """Validator for business logic of person model"""

    @classmethod
    def validate_birth_date(cls, birth_date):
        """validates birth_date > 10 years from now."""
        now = datetime.datetime.now()

        if (now.year - birth_date.year) <= 10:
            return 0
        return 1
