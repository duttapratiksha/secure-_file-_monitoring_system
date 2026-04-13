import os
from config import SENSITIVE_EXTENSIONS, SENSITIVE_KEYWORDS

def is_sensitive(filepath):
    filename = os.path.basename(filepath).lower()

    if any(filename.endswith(ext) for ext in SENSITIVE_EXTENSIONS):
        return True

    if any(word in filename for word in SENSITIVE_KEYWORDS):
        return True

    return False