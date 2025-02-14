import os
import sys
import tarfile
import datetime

def archive_logs(log_directory):
    if not os.path.isdir(log_directory):
        print(f"Error: {log_directory} is not a valid directory.")
        return

    # Create archive directory if it doesn't exist
    archive_directory = os.path.join(log_directory, "archive")
    os.makedirs(archive_directory, exist_ok=True)

    # Create tar.gz file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(archive_directory, archive_name)

    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_directory, arcname=os.path.basename(log_directory))

    # Log the archive creation
    log_file = os.path.join(archive_directory, "archive_log.txt")
    with open(log_file, "a") as log:
        log.write(f"{timestamp}: Archived logs to {archive_name}\n")

    print(f"Logs have been archived to {archive_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: log_archive <log-directory>")
        sys.exit(1)

    log_directory = sys.argv[1]
    archive_logs(log_directory)
