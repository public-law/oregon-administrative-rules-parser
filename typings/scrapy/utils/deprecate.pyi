"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""Some helpers for deprecation messages"""
def attribute(obj, oldattr, newattr, version=...):
    ...

def create_deprecated_class(name, new_class, clsdict: Optional[Any] = ..., warn_category=..., warn_once: bool = ..., old_class_path: Optional[Any] = ..., new_class_path: Optional[Any] = ..., subclass_warn_message=..., instance_warn_message=...):
    """
    Return a "deprecated" class that causes its subclasses to issue a warning.
    Subclasses of ``new_class`` are considered subclasses of this class.
    It also warns when the deprecated class is instantiated, but do not when
    its subclasses are instantiated.

    It can be used to rename a base class in a library. For example, if we
    have

        class OldName(SomeClass):
            # ...

    and we want to rename it to NewName, we can do the following::

        class NewName(SomeClass):
            # ...

        OldName = create_deprecated_class('OldName', NewName)

    Then, if user class inherits from OldName, warning is issued. Also, if
    some code uses ``issubclass(sub, OldName)`` or ``isinstance(sub(), OldName)``
    checks they'll still return True if sub is a subclass of NewName instead of
    OldName.
    """
    class DeprecatedClass(new_class.__class__):
        ...
    
    

def _clspath(cls, forced: Optional[Any] = ...):
    ...

DEPRECATION_RULES = [('scrapy.telnet.', 'scrapy.extensions.telnet.')]
def update_classpath(path):
    """Update a deprecated path from an object with its new location"""
    ...

def method_is_overridden(subclass, base_class, method_name):
    """
    Return True if a method named ``method_name`` of a ``base_class``
    is overridden in a ``subclass``.

    >>> class Base(object):
    ...     def foo(self):
    ...         pass
    >>> class Sub1(Base):
    ...     pass
    >>> class Sub2(Base):
    ...     def foo(self):
    ...         pass
    >>> class Sub3(Sub1):
    ...     def foo(self):
    ...         pass
    >>> class Sub4(Sub2):
    ...     pass
    >>> method_is_overridden(Sub1, Base, 'foo')
    False
    >>> method_is_overridden(Sub2, Base, 'foo')
    True
    >>> method_is_overridden(Sub3, Base, 'foo')
    True
    >>> method_is_overridden(Sub4, Base, 'foo')
    True
    """
    ...
