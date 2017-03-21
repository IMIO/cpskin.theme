from plone.resource.traversal import ResourceTraverser


class ThemeLessTraverser(ResourceTraverser):
    """The theme traverser.

    Allows traveral to /++themeless++<name> using ``plone.resource`` to fetch
    things stored either on the filesystem or in the ZODB.
    """
    name = 'themeless'
