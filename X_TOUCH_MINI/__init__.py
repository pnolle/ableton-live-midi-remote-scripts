import Live
from .X_TOUCH_MINI import X_TOUCH_MINI


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return X_TOUCH_MINI(c_instance)

# local variables:
# tab-width: 4
