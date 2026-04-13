from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

from logger_util import create_log_file, write_log
from helper import is_sensitive
from integrity import load_hashes, save_hashes, calculate_hash

path = r"C:\SFTMSTest"

hashes = load_hashes()

class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            status = "ALERT" if is_sensitive(event.src_path) else "SAFE"
            file_hash = calculate_hash(event.src_path)

            if file_hash:
                hashes[event.src_path] = file_hash
                save_hashes(hashes)

            write_log("CREATED", event.src_path, status=status, integrity="BASELINE")

    def on_modified(self, event):
        if not event.is_directory:
            status = "ALERT" if is_sensitive(event.src_path) else "SAFE"

            new_hash = calculate_hash(event.src_path)
            old_hash = hashes.get(event.src_path)

            integrity = "OK"
            if old_hash and new_hash and old_hash != new_hash:
                integrity = "TAMPERED"

            hashes[event.src_path] = new_hash
            save_hashes(hashes)

            write_log("MODIFIED", event.src_path, status=status, integrity=integrity)

    def on_deleted(self, event):
        if not event.is_directory:
            status = "ALERT" if is_sensitive(event.src_path) else "SAFE"

            if event.src_path in hashes:
                del hashes[event.src_path]
                save_hashes(hashes)

            write_log("DELETED", event.src_path, status=status, integrity="N/A")

    def on_moved(self, event):
        if not event.is_directory:
            status = "ALERT" if is_sensitive(event.src_path) else "SAFE"
            write_log("MOVED", event.src_path, event.dest_path, status, "OK")

create_log_file()

observer = Observer()
observer.schedule(MyHandler(), path, recursive=True)
observer.start()

print("Monitoring started...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()