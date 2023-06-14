from datetime import datetime

from pydantic import BaseModel, validator


class Report_Read(BaseModel):
    id: int
    message_id: int
    report_text: str
    created_at: datetime

    class Config:
        orm_mode = True


class Report_Create(BaseModel):
    message_id: int
    report_text: str

    @validator("report_text")
    def report_text_validator(cls, v):
        reports = [
            "Неуместно",
            "Оскорбительно",
            "Реклама",
            "Спам",
            "Нарушение конфиденциальности",
            "Нарушение авторских прав",
        ]
        if v not in reports:
            raise ValueError("Недопустимая причина жалобы.")

        return v
