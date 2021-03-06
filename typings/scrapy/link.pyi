"""
This type stub file was generated by pyright.
"""

"""
This module defines the Link object used in Link extractors.

For actual link extractors implementation see scrapy.linkextractors, or
its documentation in: docs/topics/link-extractors.rst
"""
class Link(object):
    """Link objects represent an extracted link by the LinkExtractor."""
    __slots__ = ...
    def __init__(self, url, text=..., fragment=..., nofollow: bool = ...):
        self.url = ...
        self.text = ...
        self.fragment = ...
        self.nofollow = ...
    
    def __eq__(self, other):
        ...
    
    def __hash__(self):
        ...
    
    def __repr__(self):
        ...
    


