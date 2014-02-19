from os import path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

GITPASTE_REPOSITORIES = path.join(path.dirname(__file__), 'repositories')

USE_SOCIAL_AVATARS = False

def generate_icon(email):
    """Generates the icon when a user is created. It should
    return the URL of the gravatar/desired avatar hosting."""
    import hashlib
    import urllib
    size = 40
    default = '/static/img/default-icon.png'
    gravatar = "http://www.gravatar.com/avatar/%s?%s" % (
            hashlib.md5(email.lower()).hexdigest(),
            urllib.urlencode({'d':default, 's':str(size)}))
    return gravatar

##### Localization
USE_TZ = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same timezone as the operating system.
# If running in a Windows environment this must be set to the same as your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


##### Authentication and Authorization
ALLOW_ANONYMOUS_POSTS = False
ALLOW_ANONYMOUS_ACCESS = True

AUTH_PROFILE_MODULE = "paste.Profile"

AUTHENTICATION_BACKENDS = (
    'social.backends.persona.PersonaAuth',
    'social.backends.open_id.OpenIdAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
   #'social.backends.google.GoogleOAuthBackend',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GooglePlusAuth',
   #'social.backends.yahoo.YahooBackend',
    'social.backends.github.GithubOAuth2',
    'social.backends.live.LiveOAuth2',
    'social.backends.yahoo.YahooOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
#GITHUB_EXTRA_DATA = [
#    ('avatar_url', 'avatar'),
#    ('login', 'login'),
#]

ADMINS = (
   ('Joel Bennett', 'Jaykul@HuddledMasses.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gitpaste.db',                  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

SITE_ID = 1

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = path.join(path.dirname(__file__), 'static')

# URL prefix for static files.
# Make sure to use a trailing slash.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'PoshCode.context_processors.use_tz',
    'PoshCode.context_processors.use_icon',
    'PoshCode.context_processors.site',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'paste.middleware.TimezoneMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'PoshCode.urls'
ROOTDIR = path.abspath(path.dirname(__file__))

TEMPLATE_DIRS = (
    path.join([ROOTDIR, 'templates']),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'paste',
    'haystack',
    'tastypie',
    'social.apps.django_app.default',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'filters': {
      'require_debug_false': {
         '()': 'django.utils.log.RequireDebugFalse'
      }
   },
   'handlers': {
      'mail_admins': {
         'level': 'ERROR',
         'filters': ['require_debug_false'],
         'class': 'django.utils.log.AdminEmailHandler'
      }
   },
   'loggers': {
      'django.request': {
         'handlers': ['mail_admins'],
         'level': 'ERROR',
         'propagate': True,
      },
   }
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': path.sep.join([path.dirname(__file__), 'whoosh', 'search-index']),
    },
}

###############################################################################
# SECRETS:
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'Ge!Y$c=\{&=^]>xtAz{W(4.08iT2,8~K9[D\9aiy)]}@7::||i'
# Get your own 

if SECRET_KEY is None:
   raise Exception("Please update settings.py and set your SECRET_KEY")