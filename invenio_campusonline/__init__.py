# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# invenio-campusonline is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""This module is used to import/export from/to the CampusOnline System."""

from .ext import InvenioCampusonline
from .version import __version__

__all__ = ('__version__', 'InvenioCampusonline')
