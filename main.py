from pywintypes import Time
from win32file import CreateFile, CloseHandle, GetFileTime, SetFileTime, GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from glob import glob
import time

def to_time(time_str, time_format = "%Y/%m/%d %H:%M:%S"):
    return Time(time.gmtime(time.mktime(time.strptime(time_str, time_format))))

def getFileTime(filename):
    handle = CreateFile(filename, GENERIC_READ, 0, None, OPEN_EXISTING, 0, 0)
    ctime, atime, mtime = GetFileTime(handle)
    CloseHandle(handle)

    return ctime, atime, mtime

def setFileTime(filename, ctime=None, mtime=None, atime=None):
    handle = CreateFile(filename, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)

    if ctime != None:
        SetFileTime(handle, CreationTime=ctime)
    if mtime != None:
        SetFileTime(handle, LastWriteTime=mtime)
    if atime != None:
        SetFileTime(handle, LastAccessTime=atime)
    
    CloseHandle(handle)


if __name__ == '__main__':
    files = glob("test.txt")

    old_date = to_time("2024/10/29 00:00:00")
    new_date = to_time("2024/10/29 00:05:00")

    offset = new_date - old_date

    for file in files:
        ctime, atime, mtime = getFileTime(file)
        setFileTime(file, ctime=ctime+offset, mtime=mtime+offset)
    