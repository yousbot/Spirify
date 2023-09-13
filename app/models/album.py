from .elasticsearch_base import ElasticsearchBase
from typing import List

class Album(ElasticsearchBase):
    INDEX_NAME = 'album'
    
    def __init__(
        self,
        id: str,
        title: str,
        cover_image: str,
        release_date: str,
        description: str,
        lectures: List[str],
        speaker: List[str],
        tags: List[str],
        likes: int
    ):
        self.id = id
        self.title = title
        self.cover_image = cover_image
        self.release_date = release_date
        self.description = description
        self.lectures = lectures
        self.speakers = speaker
        self.tags = tags
        self.likes = likes
    
    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)