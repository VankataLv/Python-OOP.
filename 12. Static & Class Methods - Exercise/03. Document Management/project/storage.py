from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __find_object(object_id, objects_collection):
        return next((o for o in objects_collection if o.id == object_id), None)

    def edit_category(self, category_id: int, new_name: str):
        s_cat = self.__find_object(category_id, self.categories)
        if s_cat:
            s_cat.edit(new_name)

    def edit_topic(self, topic_id, new_topic: str, new_storage_folder: str):
        s_topic = self.__find_object(topic_id, self.topics)
        if s_topic:
            s_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        s_doc = self.__find_object(document_id, self.documents)
        if s_doc:
            s_doc.edit(new_file_name)

    def delete_category(self, category_id: int):
        s_cat = self.__find_object(category_id, self.categories)
        if s_cat:
            self.categories.remove(s_cat)

    def delete_topic(self, topic_id: int):
        s_topic = self.__find_object(topic_id, self.topics)
        if s_topic:
            self.topics.remove(s_topic)

    def delete_document(self, document_id: int):
        s_doc = self.__find_object(document_id, self.documents)
        if s_doc:
            self.documents.remove(s_doc)

    def get_document(self, document_id: int):
        return self.__find_object(document_id, self.documents)

    def __repr__(self):
        return '\n'.join([d.__repr__() for d in self.documents])
