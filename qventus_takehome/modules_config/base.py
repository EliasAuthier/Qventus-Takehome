from dataclasses import asdict

class BaseSetting:

    def to_dict(self):
        return {str(key).upper() : value for key, value in asdict(self).items()}