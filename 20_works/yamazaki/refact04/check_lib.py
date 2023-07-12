import os
import errno

# 指定したファイルが存在しない場合、エラー発生
def check_file_exists(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)