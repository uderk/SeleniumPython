import os


def get_base_url():

    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return 'http://mydemostore.local/'
    elif env.lower() == 'product':
        return 'http://mydemostore.product.local/'
    # this env does not exist. This is only for illustration of the options of the framework
    else:
        raise Exception(f"Unknown environment{env}")
