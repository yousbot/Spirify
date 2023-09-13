from typing import List
from .elasticsearch_base import ElasticsearchBase

class Playlist(ElasticsearchBase):
    INDEX_NAME = 'playlist'
    
    def __init__(
        self,
        id: str,
        title: str,
        created_date: str,
        description: str,
        lectures: List[str],
        tags: List[str],
        created_by: str,
        cover_image: str
    ):
        self.id = id
        self.title = title 
        self.created_date = created_date
        self.description = description
        self.lectures = lectures
        self.tags = tags
        self.created_by = created_by
        self.cover_image = cover_image
        
    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)