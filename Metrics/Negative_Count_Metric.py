#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Negative_Count_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import NumericMetric

class Negative_Count_Metric(NumericMetric.NumericMetric):
    """
    Counts negative values encountered
    """

    def __init__(self, field_profile):
        """
        Constructor for the Negative_Count_Metric class
        """
        NumericMetric.NumericMetric.__init__(self, field_profile)

        self.count = 0

    def analyse(self, field_value):
        """
        """
        if field_value.actual < 0:
            self.count += 1

    def get_result(self):
        """
        """
        return self.count


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
