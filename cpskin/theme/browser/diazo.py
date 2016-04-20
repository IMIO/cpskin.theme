# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from plone.app.layout.navigation.interfaces import INavigationRoot

from plone.app.theming.utils import getCurrentTheme

HAS_MINISITE = False
try:
    from cpskin.minisite.interfaces import IInMinisite
    from cpskin.minisite.interfaces import IInPortal
    HAS_MINISITE = True
except ImportError:
    pass

import os


class DiazoView(BrowserView):

    def isInMinisite(self):
        if not HAS_MINISITE:
            return False
        return (self.isInMinisiteMode() or self.isInPortalMode())

    def isInMinisiteMode(self):
        if not HAS_MINISITE:
            return False
        request = self.request
        return IInMinisite.providedBy(request)

    def isInPortalMode(self):
        if not HAS_MINISITE:
            return False
        request = self.request
        return IInPortal.providedBy(request)

    def getCurrentTheme(self):
        return getCurrentTheme()

    def is_homepage(self):
        """
        Returns true if we are on navigation root
        """
        obj = aq_inner(self.context)
        if INavigationRoot.providedBy(obj):
            return True
        return False

    def get_environment(self):
        """
        Get value of ENV environment variable.
        Value should be : dev, staging, preprod or prod.
        """
        env = os.getenv('ENV', 'prod')
        return env.lower()
