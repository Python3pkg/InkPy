#!/usr/bin/env python
# -*- coding: utf-8 -*-






import django_rq

from inkpy import Converter


def generate_pdf(source_path, output_path, data, lang_code):
    conv = Converter(source_path, output_path, data, lang_code)
    conv.convert()


def generate_pdf_async(source_path, output_path, data):
    queue = django_rq.get_queue('inkpy')

    return queue.enqueue_call(
        func=generate_pdf,
        args=(
            source_path,
            output_path,
            data,
        ),
        timeout=600,
    ).id
