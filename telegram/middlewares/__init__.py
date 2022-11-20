from middlewares.access import AccessMiddleware
from settings.config import dp


dp.middleware.setup(AccessMiddleware())
