import os
import sys
from django.conf import settings


settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    ROOT_URLCONF="django_user_status.urls",
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "django_user_status",
    ],
    USER_STATUS_CACHE_DURATION=300,
    USER_STATUS_CACHE_KEY_PREFIX="last_seen",
)


import django

django.setup()


from django.test.runner import DiscoverRunner


def run_tests(*test_labels):
    """
    Run tests in the specified labels.
    """
    runner = DiscoverRunner(verbosity=1, interactive=False, failfast=False)
    failures = runner.run_tests(test_labels)
    sys.exit(failures)


if __name__ == "__main__":
    # Get command-line arguments, or default to your app's test path
    test_labels = sys.argv[1:] or ["django_user_status.tests"]
    run_tests(*test_labels)
