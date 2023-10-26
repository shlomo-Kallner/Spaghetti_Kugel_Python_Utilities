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
    Literal,
    Optional,
    cast,
    Sequence as SequenceType, 
    AbstractSet as SetType, 
    Mapping as MappingType
)

from spaghetti_kugel.utils.bottom_line.get.abc import (
    PathKeyType, 
    Getter
)

from spaghetti_kugel.utils.bottom_line.get.exceptions import NotFoundException

class _NotFoundSingleton:
    pass

_notFound = _NotFoundSingleton()

#TODO: Complete this Method!!!
def getSingle(obj: Any, path: SequenceType[PathKeyType], default: Union[Any,None, _NotFoundSingleton] = _notFound) -> Any:
    
    tmpObj = _notFound 

    for path_idx, path_part in enumerate(path, start=0):
        pass

    if tmpObj is _notFound:
        raise NotFoundException

#TODO: Complete this Method!!!
def getMultiple(obj: Any, path: SequenceType[SequenceType[PathKeyType]]) -> list[Any]:
    return []

