#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Total_Sum_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import NumericMetric

class Total_Sum_Metric(NumericMetric.NumericMetric):
    """
    Sums all values encountered
    """

    def __init__(self, field_profile):
        """
        Constructor for the Total_Sum_Metric class
        """
        NumericMetric.NumericMetric.__init__(self, field_profile)

        self.value = 0

    def analyse(self, field_value):
        """
        """
        # Exit if we cant determine how to sum the value
        if field_value.actual == None or self.value == self.__not_applicable__ or field_value.format == "undefined":
            return

        if field_value.format == "string":
            self.value = self.__not_applicable__
        else:
            self.value += field_value.actual


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
