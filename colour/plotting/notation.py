#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Colour Notation Systems Plotting
================================

Defines the colour notation systems plotting objects:

-   :func:`single_munsell_value_function_plot`
-   :func:`multi_munsell_value_function_plot`
"""

from __future__ import division

import numpy as np
import pylab

from colour.notation import MUNSELL_VALUE_METHODS
from colour.plotting import (
    aspect,
    bounding_box,
    display,
    figure_size)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['single_munsell_value_function_plot',
           'multi_munsell_value_function_plot']


def single_munsell_value_function_plot(function='ASTM D1535-08',
                                       **kwargs):
    """
    Plots given *Lightness* function.

    Parameters
    ----------
    function : unicode, optional
        *Munsell* value function to plot.
    \*\*kwargs : \*\*
        Keywords arguments.

    Returns
    -------
    bool
        Definition success.

    Examples
    --------
    >>> f = 'ASTM D1535-08'
    >>> single_munsell_value_function_plot(f)  # doctest: +SKIP
    True
    """

    settings = {'title': '{0} - Munsell Value Function'.format(function)}
    settings.update(kwargs)

    return multi_munsell_value_function_plot([function], **settings)


@figure_size((8, 8))
def multi_munsell_value_function_plot(
        functions=None,
        **kwargs):
    """
    Plots given *Munsell* value functions.

    Parameters
    ----------
    functions : array_like, optional
        *Munsell* value functions to plot.
    \*\*kwargs : \*\*
        Keywords arguments.

    Returns
    -------
    bool
        Definition success.

    Raises
    ------
    KeyError
        If one of the given *Munsell* value function is not found in the
        factory *Munsell* value functions.

    Examples
    --------
    >>> fs = ('ASTM D1535-08', 'McCamy 1987')
    >>> multi_munsell_value_function_plot(fs)  # doctest: +SKIP
    True
    """

    if functions is None:
        functions = ('ASTM D1535-08',
                     'McCamy 1987')

    samples = np.linspace(0, 100, 1000)
    for i, function in enumerate(functions):
        function, name = MUNSELL_VALUE_METHODS.get(function), function
        if function is None:
            raise KeyError(
                ('"{0}" "Munsell" value function not found in '
                 'factory "Munsell" value functions: "{1}".').format(
                    name, sorted(MUNSELL_VALUE_METHODS.keys())))

        pylab.plot(samples,
                   [function(x) for x in samples],
                   label=u'{0}'.format(name),
                   linewidth=2)

    settings = {
        'title': '{0} - Munsell Functions'.format(', '.join(functions)),
        'x_label': 'Luminance Y',
        'y_label': 'Munsell Value V',
        'x_tighten': True,
        'legend': True,
        'legend_location': 'upper left',
        'x_ticker': True,
        'y_ticker': True,
        'grid': True,
        'limits': [0, 100, 0, 100]}

    settings.update(kwargs)

    bounding_box(**settings)
    aspect(**settings)

    return display(**settings)
