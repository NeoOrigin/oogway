#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Zero_Count_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import NumericMetric

class Zero_Count_Metric(NumericMetric.NumericMetric):
    """
    Counts zero values encountered
    """

    def __init__(self, field_profile):
        """
        Constructor for the Zero_Count_Metric class
        """
        NumericMetric.NumericMetric.__init__(self, field_profile)

    def analyse(self, field_value):
        """
        """
        if field_value.actual == 0:
            self.value += 1


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
