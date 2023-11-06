#!/usr/bin/env python3


from typing import (
    Any, 
    Mapping, 
    Union, 
    Optional
)
from collections.abc import (
    Mapping as MappingABC
)


from spaghetti_kugel.utils.bottom_line.get.abc import (
    Getter as GetterABC,
    NotFoundException,
    SourceObjectType, PathKeyType, DestObjectType, DestObjectDataType
)


###########################################
# Some Common Getter Abstract Base Classes
# Todo: Complete These!!!
#

class StrPathKeyTypeGetterABC(
    Generic[SourceObjectType, DestObjectType, DestObjectDataType],
    GetterABC[SourceObjectType, str, DestObjectType, DestObjectDataType]
):

    @classmethod
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
        return isinstance(path_key, str) and len(path_key.strip()) > 0


class IntAndSlicePathKeyTypeGetterABC(
    Generic[SourceObjectType, DestObjectType, DestObjectDataType],
    GetterABC[SourceObjectType, Union[int,slice], DestObjectType, DestObjectDataType]
):

    @classmethod
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
        return isinstance(path_key, (int,slice))


###########################################
# Some Common Getters
# Todo: Complete These!!!
#

class StrObjectAttrGetter(StrPathKeyTypeGetterABC[Any, Any, Any]):
    
    @classmethod
    def validate_source_object_type(cls, obj: Any) -> bool:
        """
            validate_source_object_type 
            
            Validate the Source Object's Type 
            for Getter SubType retrival Compatibility.

            NOTE 
            ----
            As the `SourceObjectType` is `Any`,
            this method is a No-Op and Always
            returns `True`.

            Parameters
            ----------
            obj : SourceObjectType
                The Source Object to validate it's type.

            Returns
            -------
            bool
                `True` if `obj`'s Type is Valid and `False` otherwise.
        """        

        return True

    def get_from_source_object(self, obj: Any) -> Any:
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
        
        return getattr(obj, self.path_key)


class StrObjectAttrWithDefaultGetter(StrObjectAttrGetter):

    def __init__(self, path_key: str, default: Optional[Any] = None) -> None:
        super().__init__(path_key)
        self._default: Optional[Any] = default

    def get_from_source_object(self, obj: Any) -> Optional[Any]:
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
        
        return getattr(obj, self.path_key, self._default)
        


    


class StrMappingKeyGetter(StrPathKeyTypeGetterABC[Mapping[str, Any], Any, Any]):
    
    @classmethod
    def validate_source_object_type(cls, obj: Any) -> bool:
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

        return isinstance(obj, MappingABC)

    def get_from_source_object(self, obj: Mapping[str, Any]) -> Any:
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
        
        return obj.get(self.path_key)