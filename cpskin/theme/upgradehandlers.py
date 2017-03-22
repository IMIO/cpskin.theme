# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('cpskin.theme')


def upgrade_to_less(context):
    context.runAllImportStepsFromProfile('profile-collective.lesscss:default')
    context.runImportStepFromProfile(
        'profile-cpskin.theme:default',
        'registry'
    )
    context.runImportStepFromProfile(
        'profile-cpskin.theme:default',
        'lessregistry'
    )
    logger.info('LESS files installed and configurations done !')
