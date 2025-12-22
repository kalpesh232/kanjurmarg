from typing import Dict
from threading import Lock

documents : Dict[str, str] = {}
document_locks : Dict[str,Lock] = {}