#!/usr/bin/env python

import sys
import settings

from mkondo import backup,amazons3

storage = amazons3.SimpleStorage(settings.AWS_ACCESS_KEY, settings.AWS_SECRET_KEY)
backup = backup.SimpleBackup(settings.DATA_DIRECTORY, storage.send_file)

backup.backup(dir_name=settings.DATA_DIRECTORY, 
				file_filter='gz',
				bucket_name=settings.AWS_BACKUP_BUCKET, 
				path_prefix=settings.DATA_DIRECTORY)
