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


SourceObjectType = TypeVar('SourceObjectType')
PathKeyType = TypeVar('PathKeyType', bound=Union[str, int, 'Getter'])
DestObjectType = TypeVar('DestObjectType')
DestObjectDataType = TypeVar('DestObjectDataType')


class Getter(Generic[SourceObjectType, PathKeyType, DestObjectType, DestObjectDataType],ABC):

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
        """
            validate_source_object_type 
            
            Validate the Source Object's Type 
            for Getter SubType retrival Compatibility.

            Parameters
            ----------
            obj : SourceObjectType
                The Source Object to validate it's type.

            Returns
            -------
            bool
                `True` if `obj`'s Type is Valid and `False` otherwise.
        """        
        pass

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

    @abstractmethod
    def get_from_source_object(self, obj: SourceObjectType) -> DestObjectDataType:
        """
            get_from_source_object 

            #TODO Complete this DocString!!!
            
            Retrieve the Member/Element/Property at 
            `self.path_key` from the source object `obj`.

            Parameters
            ----------
            obj : SourceObjectType
                _description_

            Returns
            -------
            DestObjectType
                _description_
        """        
        pass

    def parse_dest_object_data(self, data: DestObjectDataType) -> DestObjectType:
        """
            parse_dest_object_data _summary_

            #TODO Complete this DocString!!!

            Parameters
            ----------
            data : DestObjectDataType
                _description_

            Returns
            -------
            DestObjectType
                _description_
        """        
        return cast(DestObjectType, data)

    def get(self, src: SourceObjectType) -> DestObjectType:
        """
            get _summary_

            #TODO Complete this DocString!!!

            Parameters
            ----------
            src : SourceObjectType
                _description_

            Returns
            -------
            DestObjectType
                _description_
        """        

        if not self.validate_source_object_type(src):
            raise TypeError(
                " ".join(
                    [
                        f"Getter SubClass [{self.__class__.__name__}]",
                        "does not support retriving",
                        f"[{self.path_key}] from `src` of type",
                        f"[{type(src)}]!"
                    ]
                )
            )

        else:
            try:
                data: DestObjectDataType = self.get_from_source_object(src)

            except Exception as e:
                raise ValueError(
                    f"Failed to retrieve [{self.path_key}]!!"
                ) from e

            else:

                try:
                    ret: DestObjectType = self.parse_dest_object_data(data)

                except Exception as e:
                    raise ValueError(
                        f"Failed to parse ['{data}'] from [{self.path_key}] in `src`!!"
                    ) from e

                else:
                    return ret
            

