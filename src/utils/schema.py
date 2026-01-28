from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Document:
    doc_id : str
    source: str
    source_id: str
    created_at: datetime
    collected_at : datetime
    text: str
    author: Optional[str] = None
    url : Optional[str] = None
