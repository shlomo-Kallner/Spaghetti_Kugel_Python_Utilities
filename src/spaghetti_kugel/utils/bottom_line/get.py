#!/usr/bin/env python3

from abc import ABC, abstractmethod
from collections.abc import (
    Sequence as SequenceABC, 
    Set as SetABC, 
    Mapping as MappingABC
)
from typing import (
    Any, 
    Union, 
    Generic, 
    TypeVar, 
    Type, 
    ParamSpec,
    Sequence as SequenceType, 
    AbstractSet as SetType, 
    Mapping as MappingType
)


SourceObjectType = TypeVar('SourceObjectType')
PathKeyType = TypeVar('PathKeyType', bound=Union[str, int, 'Getter'])
DestObjectType = TypeVar('DestObjectType')


class Getter(Generic[SourceObjectType, PathKeyType, DestObjectType],ABC):

    def __init__(self, path_key: PathKeyType) -> None:
        self._path_key : PathKeyType = path_key

    @property
    def path_key(self) -> PathKeyType:
        return self._path_key

    @path_key.setter
    def path_key(self, _: PathKeyType) -> None:
        raise AttributeError("path_key is READ-ONLY!!", name="path_key", obj=self)

    @path_key.deleter
    def path_key(self) -> None:
        raise AttributeError("path_key is READ-ONLY!!", name="path_key", obj=self)

    @classmethod
    @abstractmethod
    def validate_source_object_type(cls, obj: SourceObjectType) -> bool:
        pass

    @abstractmethod
    def get_from_source_object(self, obj: SourceObjectType) -> DestObjectType:
        pass

    def parse_dest_object_data(self, data) -> DestObjectType:
        return data

