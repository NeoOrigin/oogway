#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        NumericMetric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import Metric

class NumericMetric(Metric.Metric):
    """
    """

    def __init__(self, field_profile):
        """
        """
        Metric.Metric.__init__(self, field_profile)

        self.value = 0

    def get_average(self, count, precision = 2):
        """
        """
        try:
            f = float( self.value )
            return round( f / count, precision )
        except:
            return self.value

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
