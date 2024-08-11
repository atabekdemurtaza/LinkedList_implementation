from typing import Optional

from pydantic import BaseModel, validator


class ListNode(BaseModel):
    val: int
    next: Optional["ListNode"] = None

    class Config:
        arbitrary_types_allowed = True

    @validator("val")
    def validate_val(cls, v):
        if not isinstance(v, int):
            raise ValueError("val must be an integer")
        return v

    def __repr__(self) -> str:
        return f"ListNode(val={self.val})"
