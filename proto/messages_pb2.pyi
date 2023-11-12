from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Reply(_message.Message):
    __slots__ = ["response", "value"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    response: str
    value: int
    def __init__(self, response: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
