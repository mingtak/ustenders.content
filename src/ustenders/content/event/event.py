from zope import component
from zope.app.intid.interfaces import IIntIds
from z3c.relationfield import RelationValue
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent


def move_content_to_top(obj, event):
    """
    Moves Items to the top of its folder
    """
    folder = obj.getParentNode()
    if folder != None:
        folder.moveObjectsToTop(obj.id)


def discuss_default_value(object, event):
    """ """
    request = object.REQUEST
    split_url =  request['HTTP_REFERER'].split('uid=')
    if len(split_url)>1:
        uid = split_url[1]
    else:
        return
    catalog = object.portal_catalog
    brain = catalog(UID=uid)
    if brain:
        item = brain[0]
    else:
        return
    relatedObject = item.getObject()
    intIds = component.getUtility(IIntIds)
    object.relatedItem = RelationValue(intIds.getId(relatedObject))
    notify(ObjectModifiedEvent(object))
