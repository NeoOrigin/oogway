#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Unique_Values_Metric
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

class Unique_Values_Metric(Metric.Metric):
    """
    Tracks unique values encountered
    """

    def __init__(self, field_profile):
        """
        Constructor for the Unique_Values_Metric class
        """
        Metric.Metric.__init__(self, field_profile)

        self.unique_values = Tracker()
        self.dup_values    = Tracker()

    def analyse(self, field_value):
        """
        """

        # Check if already flagged as a duplicate
        has_value = self.dup_values.has_value( field_value.actual )
        if has_value:
            self.dup_values.track( field_value.actual )
            return

        # Not flagged as a duplicate yet so check if already seen
        has_value = self.unique_values.has_value( field_value.actual )
        if has_value:
            self.dup_values.track( field_value.actual )
            self.unique_values.remove( field_value.actual )
            return

        self.unique_values.track( field_value.actual )

    def get_result(self):
        """
        """
        return self.unique_values


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
