from dataclasses import dataclass

@dataclass(slots=True)
class PostDTO:
    title: str
    content: str