#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Null_Count_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import Metric

class Null_Count_Metric(Metric.Metric):
    """
    Counts null values encountered
    """

    def __init__(self, field_profile):
        """
        Constructor for the Null_Count_Metric class
        """
        Metric.Metric.__init__(self, field_profile)

        self.count = 0

    def analyse(self, field_value):
        """
        """
        if field_value.actual == None:
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
