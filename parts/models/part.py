from django.db.models import Model, CharField, DateTimeField, IntegerField, BooleanField
from parts.models import BaseModel

class Part(BaseModel):

    class Meta: 
        db_table = 'parts'

    name = CharField(max_length=150)
    sku = CharField(max_length=30)
    description = CharField(max_length=1024)
    weight_ounces = IntegerField()
    is_active = BooleanField()
