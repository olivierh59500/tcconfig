# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from dataproperty import FloatType

from tcconfig._converter import Humanreadable


def is_invalid_param(rate, delay, loss, corrupt):
    params = [
        delay,
        loss,
        corrupt,
    ]

    is_invalid = all([
        not FloatType(param).is_type() or param == 0 for param in params
    ])

    try:
        Humanreadable(kilo_size=1000).humanreadable_to_byte(rate)
    except ValueError:
        pass
    else:
        is_invalid = False

    return is_invalid
