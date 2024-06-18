class PartsAppException(Exception):
    pass

class PartsAppModelException(PartsAppException):
    pass

class PartsAppControllerException(PartsAppException):
    pass

class PartsAppSerializerException(PartsAppException):
    pass

class PartsAppViewSetException(PartsAppException):
    pass

