
"""
Django's command-line utility for administrative tasks.
"""

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Set the default settings module for the 'django' program.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Make sure it is installed and available on your PYTHONPATH environment variable.") from exc
    execute_from_command_line(sys.argv)
