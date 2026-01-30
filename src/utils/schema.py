from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional, Dict,Any 


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
    meta : Dict[str, Any] = None 

    def to_row(self):
        return{
            "doc_id" : self.doc_id,
            "source" : self.source,
            "source_id" : self.source_id,
            "created_at" : self.created_at.isoformat(),
            "collected_at" : self.collected_at.isoformat(),
            "text" : self.text,
            "author": self.author,
            "url" : self.url,       
            "meta":self.meta or {},
        }

