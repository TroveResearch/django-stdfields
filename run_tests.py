# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management import call_command

def main():
    settings.configure(
        INSTALLED_APPS = (
            'django.contrib.contenttypes',
            'stdfields',
        ),
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3'
            }
        }
    )

    # Fire off the tests
    call_command('test', 'stdfields')

if __name__ == '__main__':
    main()