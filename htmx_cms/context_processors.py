import math
from collections import defaultdict
from shutil import disk_usage
from django.conf import settings
from . import git_commit_id, __version__

TIMESTAMP = settings.TIMESTAMP


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def system_statistics(request, *args, **kwargs):
    context = {}
    if request.user.is_superuser:
        context = {
            'system__started': TIMESTAMP,
            'system__df': convert_size(disk_usage(__file__).free),
            'system__version': __version__,
            'system__commit_id': git_commit_id,
        }
    return context
