from pydantic import BaseModel, field_validator


class Category(BaseModel):
    name: str
    color: str


class Task(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    category: Category
    internal_note: str | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Заголовок должен содержать не менее 3 символов")
        return value


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    category: Category
