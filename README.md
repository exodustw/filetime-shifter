# Filetime-Shifter: Batch Modification for File Timestamps on Windows

`Filetime-Shifter` is a tool for batch modification of Windows file timestamps, specifically the creation time (`ctime`), modification time (`mtime`), and access time (`atime`). It uses the Python `win32file` API, making it ideal for scenarios where you need to correct file timestamps to match actual creation or modification times.

## Background knowledge

- **ctime**: The file's creation timestamp, indicating when the file was first created.
- **mtime**: The file's last modification timestamp, representing the last time the file's content was changed.
- **atime**: The file's last access timestamp, indicating the last time the file was opened or read.

## Motivation

Due to an inaccurate time setting on my action camera, the timestamps on my photos and videos didn’t accurately reflect when they were captured. I developed this tool to batch adjust file timestamps, making it easy to offset the times as needed.

## Usage

### Functions

- `to_time(time_str, time_format="%Y/%m/%d %H:%M:%S")`: Converts a time string to `pywintypes.Time` format, in order to compatible with `setFileTime`.
- `getFileTime(filename)`: Retrieves the `ctime`, `atime`, and `mtime` of a file.
- `setFileTime(filename, ctime=None, mtime=None, atime=None)`: Modifies file timestamps; any parameter set to `None` will leave the corresponding timestamp unchanged.

### Basic Usage of Functions

You can directly use the `setFileTime(filename, ctime, mtime, atime)` function to set the desired creation, modification, and access times for a specified file. Pass `None` for `ctime`, `mtime`, or `atime` to leave that timestamp unchanged.

For example, if you want to modify `ctime`:
```python
file = "example.txt"
ctime = to_time("2024/10/29 00:00:00")
setFileTime(file, ctime)
```

### Batch Adjustments Using Time Offset

To apply a time offset to multiple files, refer to the example in the `__main__` function:
1. Set two timestamps: the current timestamp (`old_date`) and the target timestamp (`new_date`).
2. Calculate the time offset (`offset`), then add this offset to the creation and modification times of each file.

```python
from glob import glob

files = glob("<path_to_your_file_directory>/*") # specify the directory containing the files
old_date = to_time("2024/10/29 00:10:00")        # original timestamp
new_date = to_time("2024/10/29 00:14:00")        # target timestamp
offset = new_date - old_date                    # calculate offset

for file in files:
    ctime, atime, mtime = getFileTime(file)
    setFileTime(file, ctime=ctime+offset, mtime=mtime+offset)
```

## Requirements

- **Windows Environment**: This tool relies on the `win32file` API and works only on Windows systems.
- **Python**: Python 3 is recommended.

## Notes

Ensure that the script has the appropriate permissions to access and modify the files in question; otherwise, the timestamp updates may fail.

## License

This code is free for personal use and modification.