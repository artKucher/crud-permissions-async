from sqlmodel import SQLModel


class Record(SQLModel):
    id: int
    name: str

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id
