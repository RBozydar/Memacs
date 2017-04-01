#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from memacs.gpx import GPX

PROG_VERSION_NUMBER = u"0.1"
PROG_VERSION_DATE = u"2017-03-02"
PROG_SHORT_DESCRIPTION = u"Memacs for GPX files"
PROG_TAG = u"gps"

COPYRIGHT_YEAR = "2017"
COPYRIGHT_AUTHORS = """Manuel Koell <mankoell@gmail.com>"""


if __name__ == "__main__":
    memacs = GPX(prog_version=PROG_VERSION_NUMBER,
                 prog_version_date=PROG_VERSION_DATE,
                 prog_short_description=PROG_SHORT_DESCRIPTION,
                 prog_tag=PROG_TAG,
                 copyright_year=COPYRIGHT_YEAR,
                 copyright_authors=COPYRIGHT_AUTHORS)
    memacs.handle_main()
