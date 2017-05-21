#!/usr/bin/env python
# -*- coding: utf-8 -*-






from optparse import make_option

from django.core.management.base import BaseCommand

from inkpy import api


class Command(BaseCommand):
    help = 'Convert odt file to pdf'
    option_list = BaseCommand.option_list + (
        make_option(
            '-s',
            '--source',
            dest='source',
            help='source path...',
        ),
        make_option(
            '-o',
            '--output',
            dest='output',
            help='output path...',
        ),
    )

    def handle(self, *args, **options):
        api.run_async(options.get('source'), options.get('output'), {})
