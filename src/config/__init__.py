"""Don't mess with the imports in this file, something performs deep magic and it
depend on imports here, even if they aren't used.
"""
from __future__ import absolute_import
from .celery_app import celery_app

# Fixes S3 for pipeline...
from pipeline.packager import Packager
from django.contrib.staticfiles.finders import get_finders, find


def __monkey_compile(self, paths, force=False):
        paths = self.compiler.compile(paths, force=force)
        for path in paths:
            if not self.storage.exists(path):
                if self.verbose:
                    print("Compiled file '%s' cannot be found with packager's storage. Locating it." % path)

                source_storage = self.find_source_storage(path)
                if source_storage is not None:
                    with source_storage.open(path) as source_file:
                        if self.verbose:
                            print("Saving: %s" % path)
                        self.storage.save(path, source_file)
                else:
                    raise IOError("File does not exist: %s" % path)
        return paths


def __monkey_find_source_storage(self, path):
    for finder in get_finders():
        for short_path, storage in finder.list(''):
            if short_path == path:
                if self.verbose:
                    print("Found storage: %s" % str(self.storage))
                return storage
    return None


Packager.compile = __monkey_compile
Packager.find_source_storage = __monkey_find_source_storage
