from myblog.settings.common import *
DEBUG = False
ALLOWED_HOSTS = os.environ['WEBSITE_HOSTNAME']
SECRET_KEY = os.environ["SECRET_KEY"]