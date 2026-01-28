from dataclasses import dataclass
from datetime import datetime, timezone
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
        }

doc = Document(
    doc_id="test123",
    source="reddit",
    source_id="t3_abc",
    created_at=datetime.now(timezone.utc),
    collected_at=datetime.now(timezone.utc),
    text="AAPL earnings look strong",
)
print(doc.to_row())