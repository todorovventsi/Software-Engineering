class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def find_item(id, collection):
        for item in collection:
            if id == item.id:
                return item

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        current_category = Storage.find_item(category_id, self.categories)
        current_category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        current_topic = Storage.find_item(topic_id, self.topics)
        current_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        current_doc = Storage.find_item(document_id, self.documents)
        current_doc.edit(new_file_name)

    def delete_category(self, category_id):
        current_cat = Storage.find_item(category_id, self.categories)
        self.categories.remove(current_cat)

    def delete_topic(self, topic_id):
        current_topic = Storage.find_item(topic_id, self.topics)
        self.topics.remove(current_topic)

    def delete_document(self, document_id):
        current_doc = Storage.find_item(document_id, self.documents)
        self.documents.remove(current_doc)

    def get_document(self, document_id):
        return Storage.find_item(document_id, self.documents)

    def __repr__(self):
        new_line = '\n'
        representation = [f"{doc!r}" for doc in self.documents]
        return f"{new_line.join(representation)}"
