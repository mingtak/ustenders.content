# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
from ustenders.content import interfaces


@indexer(interfaces.INotice)
def noticeTypeName_indexer(obj):
     return obj.noticeTypeName


@indexer(interfaces.INotice)
def date_indexer(obj):
     return obj.date


@indexer(interfaces.INotice)
def agency_indexer(obj):
     return obj.agency

@indexer(interfaces.INotice)
def ntype_indexer(obj):
     return obj.ntype

"""
@indexer(interfaces.INotice)
def classcod_indexer(obj):
     return obj.classcod

@indexer(interfaces.INotice)
def naics_indexer(obj):
     return obj.naics
"""

@indexer(interfaces.INotice)
def respdate_indexer(obj):
     return obj.respdate


@indexer(interfaces.INotice)
def md5_indexer(obj):
     return obj.md5


@indexer(interfaces.IClassCode)
def pCode_indexer(obj):
     return obj.pCode

@indexer(interfaces.INaics)
def naicsCode_indexer(obj):
     return obj.naicsCode

