#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import django
django.setup()
import os
import sys


if __name__ == "__main__":
    if not os.environ.get('DJANGO_ENV', False):
        raise EnvironmentError('Please define DJANGO_ENV environment variable')
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineacademy.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
