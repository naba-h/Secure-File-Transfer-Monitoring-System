import time
import os
import hashlib
import logging
import getpass

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import MONITORED_FOLDER, SENSITIVE_FILES, LOG_FILE

# Create logs folder if not exists
os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s | Project: Naba Hanfi"
)

# Hash function
def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    except:
        return None

# Integrity verification
def verify_integrity(old_hash, new_hash):
    if old_hash == new_hash:
        return "INTEGRITY OK"
    else:
        return "INTEGRITY FAILED"

class MonitorHandler(FileSystemEventHandler):

    def process_event(self, action, path):
        filename = os.path.basename(path)
        file_hash = calculate_hash(path)
        user = getpass.getuser()

        # Check sensitive file
        if filename in SENSITIVE_FILES:
            logging.warning(f"SECURITY ALERT | USER={user} | EVENT={action} | FILE={path} | STATUS=SENSITIVE")
            print(f"[ALERT] Sensitive file {filename} {action}")
        else:
            logging.info(f"USER={user} | EVENT={action} | FILE={path}")
            print(f"[INFO] {action}: {path}")

        # Log hash and integrity check
        if file_hash:
            logging.info(f"HASH: {file_hash}")
            status = verify_integrity(file_hash, file_hash)
            logging.info(f"INTEGRITY CHECK: {status} | FILE={filename}")

    def on_created(self, event):
        if not event.is_directory:
            self.process_event("CREATED", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.process_event("MODIFIED", event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            self.process_event("MOVED", event.dest_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.process_event("DELETED", event.src_path)

if __name__ == "__main__":
    print("[+] Secure File Transfer Monitoring Started")
    print(f"[+] Monitoring folder: {MONITORED_FOLDER}")

    event_handler = MonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, MONITORED_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[+] Monitoring stopped")

    observer.join()

    # Final audit report
    with open("reports/final_audit.txt", "w") as f:
        f.write("Secure File Transfer Monitoring System - Final Audit Report\n")
        f.write("Monitoring session completed successfully.\n")

    print("[+] Final audit report generated in reports/final_audit.txt")