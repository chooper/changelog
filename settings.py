import os

# Configure your settings through env vars, or change their defaults here
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///changelog.db')   # Any valid SQLAlchemy connection string
LISTEN_HOST = os.getenv('HOST',         '127.0.0.1')                # Which IP to bind to
LISTEN_PORT = os.getenv('PORT',         '5000')                     # Which port to listen on

# Flask debug mode (if DEBUG is set and not set to the string '0' then it's enabled)
DEBUG = os.getenv('DEBUG') != '0'

# Use these to enable sending problems to Sentry
SENTRY_DSN = os.getenv('SENTRY_DSN')
USE_SENTRY = SENTRY_DSN and os.getenv('USE_SENTRY') != '0'

# Loading site-specific override settings
extra_settings_path = os.getenv('CHANGELOG_SETTINGS_PATH')
if extra_settings_path is not None:
    try:
        print 'Loading user-specified settings from %s' % extra_settings_path
    except IOError:
        pass
    import imp
    extra_settings_module = imp.load_source('extra_settings', extra_settings_path)
    globals().update(dict([(key, value) for key, value in extra_settings_module.__dict__.iteritems() if not key.startswith('__')]))

try:
    print 'Starting with settings', dict([(key, value) for key, value in globals().items() if key.isupper()])
except IOError:
    pass
