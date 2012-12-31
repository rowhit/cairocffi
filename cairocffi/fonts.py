"""
    cairocffi.fonts
    ~~~~~~~~~~~~~~~

    Bindings for font-related objects.

    :copyright: Copyright 2013 by Simon Sapin
    :license: BSD, see LICENSE for details.

"""

from . import ffi, cairo, _check_status


class FontOptions(object):
    def __init__(self, _pointer=None, **values):
        if _pointer is None:
            _pointer = cairo.cairo_font_options_create()
        self._pointer = ffi.gc(_pointer, cairo.cairo_font_options_destroy)
        self._check_status()
        for name, value in values.items():
            getattr(self, 'set_' + name)(value)

    def _check_status(self):
        _check_status(cairo.cairo_font_options_status(self._pointer))

    def copy(self):
        return type(self)(cairo.cairo_font_options_copy(self._pointer))

    def merge(self, other):
        cairo.cairo_font_options_merge(self._pointer, other._pointer)
        _check_status(cairo.cairo_font_options_status(self._pointer))

    def __hash__(self):
        return cairo.cairo_font_options_hash(self._pointer)

    def __eq__(self, other):
        return cairo.cairo_font_options_equal(self._pointer, other._pointer)

    def __ne__(self, other):
        return not self == other

    equal = __eq__
    hash = __hash__

    def set_antialias(self, antialias):
        cairo.cairo_font_options_set_antialias(self._pointer, antialias)
        self._check_status()

    def get_antialias(self):
        return cairo.cairo_font_options_get_antialias(self._pointer)

    def set_subpixel_order(self, subpixel_order):
        cairo.cairo_font_options_set_subpixel_order(
            self._pointer, subpixel_order)
        self._check_status()

    def get_subpixel_order(self):
        return cairo.cairo_font_options_get_subpixel_order(self._pointer)

    def set_hint_style(self, hint_style):
        cairo.cairo_font_options_set_hint_style(self._pointer, hint_style)
        self._check_status()

    def get_hint_style(self):
        return cairo.cairo_font_options_get_hint_style(self._pointer)

    def set_hint_metrics(self, hint_metrics):
        cairo.cairo_font_options_set_hint_metrics(self._pointer, hint_metrics)
        self._check_status()

    def get_hint_metrics(self):
        return cairo.cairo_font_options_get_hint_metrics(self._pointer)
