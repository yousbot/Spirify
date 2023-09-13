from .elasticsearch_base import ElasticsearchBase
from typing import List, Dict

class Speaker(ElasticsearchBase):
    INDEX_NAME = 'speaker'
    
    def __init__(
        self, 
        id: str, 
        name: str, 
        profile_picture: str, 
        bio: str,
        lectures: List[str], 
        albums: List[str], 
        playlists: List[str], 
        tags: List[str], 
        links: List[Dict[str, str]], 
        followers: int, 
        likes: int
    ):
        
        self.id = id
        self.name = name
        self.profile_picture = profile_picture
        self.bio = bio
        self.lectures = lectures
        self.albums = albums
        self.playlists = playlists
        self.tags = tags
        self.links = links
        self.followers = followers
        self.likes = likes
        
    def to_dict(self):
        return vars(self)
    
    @classmethod
    def from_dict(cls, d: Dict):
        return cls(**d)