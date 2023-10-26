#!/usr/bin/env python3


from typing import (
    Any, 
    Union, 
    Generic, 
    TypeVar, 
    Type, 
    ParamSpec,
    Literal,
    Optional,
    cast,
    Sequence as SequenceType, 
    AbstractSet as SetType, 
    Mapping as MappingType
)

from spaghetti_kugel.utils.bottom_line.get.abc import PathKeyType

class NotFoundException(Exception):
    
    def __init__(self, path: SequenceType[PathKeyType]):
        super().__init__(path)
        self._path = path

    @property
    def path(self) -> SequenceType[PathKeyType]:
        return self._path