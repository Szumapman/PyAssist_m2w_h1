from datetime import datetime

from utility.title import Title
from utility.content import Content


class Note:
    """class for note object
    """
    def __init__(self, title: Title, content: Content, tags=[]):
        self._title = title
        self._content = content
        self.__create_time = datetime.now()
        self.__modified_time = None
        self.__tags = tags
        

    def __repr__(self):
        creation_time_str = self.__create_time.strftime("%Y-%m-%d %H:%M:%S")
        if self.__modified_time:
            modified_time_str = self.__modified_time.strftime("%Y-%m-%d %H:%M:%S")          
        tags_str = ", ".join(self.__tags) if self.__tags else "note has no tag"     
        return (
            f"Title: {self.title}\n"
            f"Content: {self.content}\n"
            f"Creation Time: {creation_time_str}\n"
            f"Last Modified Time: {modified_time_str}\n" if self.__modified_time else ""
            f"Tags: {tags_str}"
        )
    
     
    @property
    def title(self):
        return self._title
    
    
    @title.setter
    def title(self, title: Title):
        self._title = title
        self.__modified_time = datetime.now()
        
        
    @property
    def content(self):
        return self._content
    
    
    @content.setter
    def content(self, content: Content):
        self._content = content
        self.__modified_time = datetime.now()
        
    
    def add_tag(self, tag):
        self.__tags.append(tag)
        self.__modified_time = datetime.now()
    
    def remove_tag(self, tag):
        self.__tags.remove(tag)