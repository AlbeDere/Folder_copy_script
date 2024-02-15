import os
import shutil
import hashlib
import argparse
import time
import threading
import datetime


# Checking integrity using md5
def md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Folder sync function
def sync_folders(source, replica, log_file):
    with open(log_file, 'a') as log:
        # Synchronization start to file and to console
        log.write(f"--- Synchronization started at {datetime.datetime.now()} ---\n")
        print(f"--- Synchronization started at {datetime.datetime.now()} ---")

        for src_dir, dirs, files in os.walk(source):
            dst_dir = src_dir.replace(source, replica, 1)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
                log.write(f"Created directory: {dst_dir}\n")
                print(f"Created directory: {dst_dir}")

            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if not os.path.exists(dst_file) or md5(src_file) != md5(dst_file):
                    shutil.copy2(src_file, dst_dir)
                    log.write(f"Copied file: {src_file} to {dst_dir}\n")
                    print(f"Copied file: {src_file} to {dst_dir}")

        for dst_dir, dirs, files in os.walk(replica):
            src_dir = dst_dir.replace(replica, source, 1)
            if not os.path.exists(src_dir):
                shutil.rmtree(dst_dir)
                log.write(f"Removed directory: {dst_dir}\n")
                print(f"Removed directory: {dst_dir}")

            for file_ in files:
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if not os.path.exists(src_file):
                    os.remove(dst_file)
                    log.write(f"Removed file: {dst_file}\n")
                    print(f"Removed file: {dst_file}")

        # Synchronization end to file and to console
        log.write(f"--- Synchronization completed at {datetime.datetime.now()} ---\n\n")
        print(f"--- Synchronization completed at {datetime.datetime.now()} ---\n")


# Periodic synchronization
def periodic_sync(interval, source, replica, log_file):
    while True:
        sync_folders(source, replica, log_file)
        time.sleep(interval)


# Parses command line arguments with argparse
def main():
    parser = argparse.ArgumentParser(description='Synchronize two folders.')
    parser.add_argument('source', help='The source directory to sync from')
    parser.add_argument('replica', help='The replica directory to sync to')
    parser.add_argument('--interval', type=int, default=60, help='Synchronization interval in seconds')
    parser.add_argument('--log', default='sync.log', help='Path to log file')
    args = parser.parse_args()

    # Start synchronization
    sync_thread = threading.Thread(target=periodic_sync, args=(args.interval, args.source, args.replica, args.log))
    sync_thread.daemon = True
    sync_thread.start()

    # Ctrl + C to stop thread
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Synchronization stopped by user.")


if __name__ == "__main__":
    main()
