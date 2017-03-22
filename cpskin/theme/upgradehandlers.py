# -*- coding: utf-8 -*-

import logging

from cpskin.theme.setuphandlers import addCustomLessFiles

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
    logger.info('LESS files installed and configurations done !')
