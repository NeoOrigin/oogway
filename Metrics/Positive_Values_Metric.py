#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Positive_Values_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import Metric
from Profiles.Tracker import *

class Positive_Values_Metric(Metric.Metric):
    """
    Counts null values encountered
    """

    def __init__(self, field_profile):
        """
        Constructor for the Positive_Values_Metric class
        """
        Metric.Metric.__init__(self, field_profile)

        self.values = Tracker()

    def analyse(self, field_value):
        """
        """
        if field_value > 0:
            self.values.track( field_value.actual )

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
