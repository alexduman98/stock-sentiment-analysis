from datetime import datetime, timezone
from src.utils.schema import Document

def test_document_row() :
    doc  = Document(
        doc_id = "test1",
        source="reddit",
        source_id = "t1_ab",
        created_at = datetime(2026,1,28,0,0 , tzinfo = timezone.utc),
        collected_at=datetime(2026,1,28,0,1, tzinfo = timezone.utc),
        text="AAPL going up",
        author = None,
        url = None,
        meta = {
                "subreddit": "wallstreetbets",
                "score": 123,
                "num_comments": 45,
                "over_18": False,
}
    )
    
    row = doc.to_row()
    assert row["doc_id"]  == "test1"
    assert row["source"] == "reddit"
    assert isinstance(row["text"],str)
