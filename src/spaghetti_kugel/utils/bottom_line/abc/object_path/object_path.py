#!/usr/bin/env python3

from abc import ABC, abstractmethod
from collections.abc import (
    Sequence as SequenceABC, 
    Set as SetABC, 
    Mapping as MappingABC,
    Hashable as HashableABC
)
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


PathKeyType = TypeVar('PathKeyType', bound=Union[str, int, slice, HashableABC, 'PathAccessor'])

class PathAccessor(Generic[PathKeyType], ABC):

    def __init__(self, path_key: PathKeyType) -> None:

        if self.__class__.validate_path_key_type(path_key):
            self._path_key : PathKeyType = self.__class__.parse_path_key(path_key)

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
    def parse_path_key(cls, path_key: PathKeyType) -> PathKeyType:
        """
            parse_path_key _summary_

            #TODO Complete this DocString!!!

            Parameters
            ----------
            path_key : PathKeyType
                _description_

            Returns
            -------
            PathKeyType
                _description_
        """        
        return cast(PathKeyType, path_key)

    @classmethod
    @abstractmethod
    def validate_path_key_type(cls, path_key: PathKeyType) -> bool:
        """
            validate_path_key_type 
            
            Validate the Path_Key's Type 
            for Getter SubType retrival Compatibility.

            Parameters
            ----------
            path_key : PathKeyType
                The Path_Key Object to validate it's type.

            Returns
            -------
            bool
                `True` if `path_key`'s Type is Valid and `False` otherwise.
        """        
        pass

    
