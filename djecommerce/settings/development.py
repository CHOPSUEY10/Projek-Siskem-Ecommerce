from .base import *
from collections import Counter

DEBUG = True

# jika ingin menjadi host, tambahkan IP address host ke ALLOWED_HOST
ALLOWED_HOSTS = ['127.0.0.1','192.168.136.94'] 

INSTALLED_APPS += [
    'debug_toolbar',
    'crispy_bootstrap4',   
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', 'allauth.account.middleware.AccountMiddleware',
]

MEDIA_URL = '/img/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_in_env', 'img')

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4" 

# Checking if there's duplicate apps

duplicates = [app for app, count in Counter(INSTALLED_APPS).items() if count > 1]
if duplicates:
    print("🚨 DUPLICATE APPS FOUND:", duplicates)
else:
    print("✅ No duplicate apps detected.")


# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True




DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
