from django.db.models import Model, AutoField

class BaseModel(Model):

    class Meta: 
        abstract = True

    id = AutoField(primary_key=True)
