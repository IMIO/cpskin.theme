# -*- coding: utf-8 -*-

from plone import api
from plone.resource.interfaces import IResourceDirectory
from six import StringIO
from zope.component import getUtility
import logging

from cpskin.theme.setuphandlers import addCustomLessFiles
from cpskin.theme.setuphandlers import CUSTOM_FOLDER_NAME

logger = logging.getLogger('cpskin.theme')


def upgrade_to_less(context):
    context.runAllImportStepsFromProfile('profile-collective.lesscss:default')
    context.runImportStepFromProfile(
        'profile-cpskin.theme:default',
        'plone.app.registry'
    )
    context.runImportStepFromProfile(
        'profile-cpskin.theme:default',
        'lessregistry'
    )
    addCustomLessFiles()
    migrate_existing_custom_to_less()
    logger.info('LESS files installed and configurations done !')


def migrate_existing_custom_to_less():
    portal_resources = getUtility(IResourceDirectory, name='persistent')
    portal_skins = api.portal.get_tool('portal_skins')
    custom = getattr(portal_skins, 'custom', None)
    if not custom:
        return
    if not 'ploneCustom.css' in custom.objectIds():
        # getattr() doesn't work here : FSDTMLMethod is always returned for
        # ploneCustom.css even if it doesn't exist.
        return
    ploneCustom = getattr(custom, 'ploneCustom.css', None)
    customCSS = ploneCustom.read()
    folder = portal_resources[CUSTOM_FOLDER_NAME]
    folder.writeFile(
        'styles.less',
        StringIO(customCSS),
    )
    title = ploneCustom.title
    ploneCustom.manage_edit(data='/*\nMigrated to LESS.\n*/', title=title)
    logger.info('ploneCustom.css migrated to styles.less in portal_resources')
