# Folder Synchronization Script

This Python script enables you to synchronize two folders, ensuring that their contents remain identical. It utilizes MD5 hashing to compare files and efficiently copy only the changed or missing files between the source and replica directories.

## Features

- **MD5 Hashing**: Files are compared using MD5 hashes to detect changes.
- **Periodic Synchronization**: You can set a synchronization interval to automatically check for updates at specified intervals.
- **Logging**: All synchronization activities are logged to a file for easy tracking and debugging.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/folder-sync.git
    ```

2. **Navigate to the cloned directory:**

    ```bash
    cd folder-sync
    ```

## Usage

Run the script with the following command:

```bash
python sync.py [source] [replica] [--interval INTERVAL] [--log LOG_FILE]
```

- `source`: The source directory to sync from.
- `replica`: The replica directory to sync to.
- `--interval INTERVAL`: *(Optional)* Synchronization interval in seconds (default is 60).
- `--log LOG_FILE`: *(Optional)* Path to the log file (default is `sync.log`).

## Example

To synchronize two folders `source` and `replica` every 120 seconds and log activities to `sync_log.txt`, run:

```bash
python sync.py source replica --interval 120 --log sync_log.txt
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or create a pull request.

