#  -*- coding: utf-8 -*-
#
#  Copyright (C) 2020-2021 ProGeek
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import datetime
from enum import IntEnum

log = logging.getLogger('growatt_logging')


class Timespan(IntEnum):
    hour = 0
    day = 1
    month = 2
    year = 3
    total = 4

    def format_date(self, date=None):

        if date is None:
            date = datetime.datetime.now()

        match self:
            case Timespan.day:
                return date.strftime("%Y-%m-%d")
            case Timespan.month:
                return date.strftime("%Y-%m")
            case Timespan.year:
                return date.strftime("%Y")
            case Timespan.total:
                return ""
            case _:
                raise ValueError(self)
