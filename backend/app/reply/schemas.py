from pydantic import BaseModel, validator
from datetime import datetime
import re
import pymorphy2


morph = pymorphy2.MorphAnalyzer()


class Reply_Read(BaseModel):
    id: int
    message_id: int
    reply_text: str
    created_at: datetime

    class Config:
        orm_mode=True
        

class Reply_EN_Create(BaseModel):
    message_id: int
    reply_text: str

    @validator('reply_text')
    def reply_text_validator(cls, v):
        if len(v) < 100:
            raise ValueError('The message must be at least 100 characters long.')
        if len(v) > 30000:
            raise ValueError('The message must not contain more than 30000 characters.')
            
        email_regex = re.compile(r'(?i)\b(https?|www|[a-zа-я0-9]+\.(com|ru|net|io|me|org|edu|info|biz|co|gov|space|website|site|su|store|pro|online|xyz|fun|tech|shop))\b')
        if email_regex.search(v):
            raise ValueError('The message must not contain links.')
        
        if re.search(r'[@]', v):
            raise ValueError('The message must not contain forbidden characters.')

        english_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        total_chars = len(v)
        english_chars_count = sum(1 for char in v if char in english_chars)
        if english_chars_count / total_chars < 0.7:
            raise ValueError('The message must be in English.')

        if re.search(r'\b(?i)[a-zа-я0-9._%+-]+@[a-zа-я0-9.-]+\.[a-z]{2,}\b', v):
            raise ValueError('The message must not contain emails.')
        
        profanity_regex = re.compile(r'(?i)\b(cunt|twat|whore|slut|nigger|nigga|faggot|homo|retard|autistic|virgin|incel|simp|chink|spic|kike|wetback|fag|dyke|queer|whore|motherfucker)\b')
        if profanity_regex.search(v):
            raise ValueError('The message must not contain forbidden words.')
    
        return v

class Reply_RU_Create(BaseModel):
    message_id: int
    reply_text: str

    @validator('reply_text')
    def reply_text_validator(cls, v):
        if len(v) < 100:
            raise ValueError('Сообщение не должно содержать менее 100 символов.')
        if len(v) > 30000:
            raise ValueError('Сообщение не должно содержать более 30000 символов.')
            
        email_regex = re.compile(r'(?i)\b(https?|www|[a-zа-я0-9]+\.(com|ru|net|io|me|org|edu|info|biz|co|gov|space|website|site|su|store|pro|online|xyz|fun|tech|shop))\b')
        if email_regex.search(v):
            raise ValueError('Сообщение не должно содержать ссылки.')

        symbols_regex = re.compile(r'[@]')    
        if symbols_regex.search(v):
            raise ValueError('Сообщение не должно содержать запрещённые символы.')

        russian_chars = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
        total_chars = len(v)
        russian_chars_count = sum(1 for char in v if char in russian_chars)
        if russian_chars_count / total_chars < 0.7:
            raise ValueError('Сообщение должно быть на русском языке.')

        if re.search(r'\b(?i)[a-zа-я0-9._%+-]+@[a-zа-я0-9.-]+\.[a-z]{2,}\b', v):
            raise ValueError('Сообщение не должно содержать эмейлы.')

        profanity_regex = re.compile(r'(?i)\b(наркотик|негр|нигер|ниггер|нигга|nigger|nigga|faggot|пидор|пидорас|педик|гомик|петух|чурка|хач|хохол|хиджаб|фашист|нацист|бандеровец|арийский|жид|семит|скинхед|расист|кафр|шварц|мулла|даун|аутист|девственник|симп|инцел|cunt|куколд)\b')
        if any(profanity_regex.search(word) or profanity_regex.search(morph.parse(word)[0][2]) for word in v.split()):
            raise ValueError('Сообщение не должно содержать запрещённые слова.')

        return v
