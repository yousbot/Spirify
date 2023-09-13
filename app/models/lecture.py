from .elasticsearch_base import ElasticsearchBase
from typing import List, Dict

class Lecture(ElasticsearchBase):    
    INDEX_NAME = 'lecture'
    
    def __init__(
        self,
        id: str,
        title: str,
        speaker: List[str],
        category: List[str],
        tags: List[str],
        duration: int,
        lecture_cover: str,
        upload_date: str,
        audio_date: str,
        audio_url: str,
        description: str,
        transcript: List[Dict[str, str]],
        location: str,
        mentions: List[str],
        recommendations: List[str],
        likes: int,
        views: int
    ):
        self.id = id
        self.title = title
        self.speaker = speaker
        self.category = category
        self.tags = tags
        self.duration = duration
        self.lecture_cover = lecture_cover
        self.upload_date = upload_date
        self.audio_date = audio_date
        self.audio_url = audio_url
        self.description = description
        self.transcript = transcript
        self.location = location
        self.mentions = mentions
        self.recommendations = recommendations
        self.likes = likes
        self.views = views
        
    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_dict(cls, d: Dict):
        return cls(**d)