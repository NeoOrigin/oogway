#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Avg_Value_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import NumericMetric

class Avg_Value_Metric(NumericMetric.NumericMetric):
    """
    Averages values encountered
    """

    def __init__(self, field_profile):
        """
        Constructor for the Avg_Value_Metric class
        """
        Metric.Metric.__init__(self, field_profile)

        self.value = 0
        self.count = 0

    def analyse(self, field_value):
        """
        """
        self.value += field_value.actual
        self.count += 1

    def get_result(self):
        """
        """
        if self.count > 0:
            return float( self.value ) / self.count
        else:
            return self.value


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
