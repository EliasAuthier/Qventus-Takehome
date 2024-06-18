from django.db.models import Model
from parts.exceptions import PartsAppControllerException

class BaseController:

    model_cls: Model = None

    def get_all(self):
        if self.model_cls == None:
            raise PartsAppControllerException(f"Class Model not defined for Controller {type(self)}")
        return self.model_cls.objects.all()