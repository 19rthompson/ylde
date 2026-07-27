from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Comic:
    num: int
    title: str
    safe_title: str
    publication_date: str
    transcript: str
    alt_text: str
    image_url: str
    link: str
    news: str
    explanation_text: str
    source_url: str

    retrieved_date: datetime = field(default_factory=datetime.now)
    def update_retrieved_date(self) -> None:
        self.retrieved_date = datetime.now()