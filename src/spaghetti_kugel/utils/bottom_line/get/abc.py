#!/usr/bin/env python3

from abc import abstractmethod
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



from spaghetti_kugel.utils.bottom_line.abc.object_path import (
    PathKeyType,
    PathAccessor,
    NotFoundException
)



# PathKeyType = TypeVar('PathKeyType', bound=Union[str, int, slice, 'Getter'])
SourceObjectType = TypeVar('SourceObjectType')
DestObjectType = TypeVar('DestObjectType')
DestObjectDataType = TypeVar('DestObjectDataType')


class Getter(Generic[SourceObjectType, PathKeyType, DestObjectType, DestObjectDataType], PathAccessor[PathKeyType]):

    def __init__(self, path_key: PathKeyType) -> None:
        super().__init__(path_key)

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
            

