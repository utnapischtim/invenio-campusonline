# -*- coding: utf-8 -*-
#
# Copyright (C) 2021-2022 Graz University of Technology.
#
# invenio-campusonline is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""This module is used to import/export from/to the CampusOnline System."""

from .ext import InvenioCampusonline

__version__ = '0.1.0'

__all__ = ('__version__', 'InvenioCampusonline')
