from .database_connector import DatabaseConnector

class ElasticsearchBase:
    INDEX_NAME = None  # To be overridden by subclasses
    es_connector = DatabaseConnector(db_type="elasticsearch", environment="prod")
    es_connector.connect()
    es = es_connector.connection

    def to_dict(self):
        raise NotImplementedError("Subclasses should implement this method")

    @classmethod
    def from_dict(cls, d):
        raise NotImplementedError("Subclasses should implement this method")

    def save(self):
        self.es.index(index=self.INDEX_NAME, doc_type='_doc', id=self.id, body=self.to_dict())

    @classmethod
    def get_by_id(cls, doc_id):
        query = {
            "query": {
                "term": {
                    "id.keyword": doc_id
                }
            }
        }
        response = cls.es.search(index=cls.INDEX_NAME, body=query)
        hits = response.get("hits", {}).get("hits", [])
        if hits:
            return cls.from_dict(hits[0]["_source"])
        else:
            return None

    @classmethod
    def delete_by_id(cls, doc_id):
        cls.es.delete(index=cls.INDEX_NAME, doc_type='_doc', id=doc_id)
