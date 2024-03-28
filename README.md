# Folder Synchronization Script

This Python script enables you to synchronize two folders, ensuring that their contents remain identical. It utilizes MD5 hashing to compare files and efficiently copy only the changed or missing files between the source and replica directories.

## Features

- **MD5 Hashing**: Files are compared using MD5 hashes to detect changes.
- **Periodic Synchronization**: You can set a synchronization interval to automatically check for updates at specified intervals.
- **Logging**: All synchronization activities are logged to a file for easy tracking and debugging.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/folder-sync.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd folder-sync
    ```


## Usage

Run the script with the following command:

```bash
python sync.py [source] [replica] [--interval INTERVAL] [--log LOG_FILE]

