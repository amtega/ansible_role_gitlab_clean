# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from datetime import datetime


def gitlab_clean_older(date_str, seconds):
    """Check if a date is older than a number of seconds.

    Args:
        date_str (string): date to check
        seconds (int): seconds

    Returns:
        bool: true if date is older than seconds and false if not
    """
    date_param = datetime.strptime(date_str[0:23], "%Y-%m-%dT%H:%M:%S.%f")
    current_date = datetime.today()
    return (current_date - date_param).seconds >= seconds


class TestModule(object):
    """Ansible gitlab_clean tests."""

    def tests(self):
        return {
            'gitlab_clean_older': gitlab_clean_older
        }
