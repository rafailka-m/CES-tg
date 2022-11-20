from middlewares.access import AccessMiddleware
from middlewares.fsm_finish import FinishStateMiddleware
from settings.config import dp


dp.middleware.setup(AccessMiddleware())
dp.middleware.setup(FinishStateMiddleware())
