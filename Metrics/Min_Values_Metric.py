#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Min_Values_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import Metric
import Profiles.Tracker

import bisect

class Min_Values_Metric(Metric.Metric):
    """
    Tracks the lowest values encountered
    """

    def __init__(self, field_profile, limit = 10):
        """
        Constructor for the Min_Values_Metric class
        """
        Metric.Metric.__init__(self, field_profile)

        self.values = []
        self.limit = limit

    def analyse(self, field_value):
        """
        """

        # Sort our value into the sliding window
        bisect.insort( self.values, field_value.actual )

        # If our sliding window is so big resize it
        if len( self.values ) > self.limit:
            self.values = self.values[:-2]

    def get_result(self):
        """
        """
        return self.values


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
