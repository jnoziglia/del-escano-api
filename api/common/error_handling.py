class AppErrorBaseClass(Exception):
    pass


class ObjectNotFound(AppErrorBaseClass):
    pass


class BadRequest(AppErrorBaseClass):
    pass


class ObjectAlreadyExists(AppErrorBaseClass):
    pass


class Unauthorized(AppErrorBaseClass):
    pass
