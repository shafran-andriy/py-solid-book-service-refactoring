import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


class DisplayBook(Book):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)    
        
    def display_console(self, display_type: str) -> None:    
        if display_type == "console":
            print(self.content)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
        
    def display_reverse(self, display_type: str) -> None:
        if display_type == "reverse":
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown display type: {display_type}")

  
class PrintBook(Book):
    def __init__(self, title: str, content: str):
        super().__init__(title, content)    
        
    def print_console(self, print_type: str) -> None:
        if print_type == "console":
            print(f"Printing the book: {self.title}...")
            print(self.content)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
        
    def print_reverse(self, print_type: str) -> None:
        if print_type == "reverse":
            print(f"Printing the book in reverse: {self.title}...")
            print(self.content[::-1])
        else:
            raise ValueError(f"Unknown print type: {print_type}")


class SerializeJsonBook(Book):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)    
        
    def serialize_json(self, serialize_type: str) -> str:
        if serialize_type == "json":
            return json.dumps({"title": self.title, "content": self.content})
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

     
class SerializeXmlBook(Book):
    def __init__(self, title: str, content: str) -> None:
        super().__init__(title, content)    
        
    def serialize_xml(self, serialize_type: str) -> str:
        if serialize_type == "xml":
            root = ET.Element("book")
            title = ET.SubElement(root, "title")
            title.text = self.title
            content = ET.SubElement(root, "content")
            content.text = self.content
            return ET.tostring(root, encoding="unicode")
        else:
            raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: DisplayBook | PrintBook | SerializeJsonBook | SerializeXmlBook,
        commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display" and method_type == "console":
            book.display_console(method_type)
        elif cmd == "display" and method_type == "reverse":
            book.display_reverse(method_type)
        elif cmd == "print" and method_type == "console":
            book.print_console(method_type)
        elif cmd == "print" and method_type == "reverse":
            book.print_reverse(method_type)
        elif cmd == "serialize" and method_type == "json":
            return book.serialize_json(method_type)
        elif cmd == "serialize" and method_type == "xml":
            return book.serialize_xml(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
