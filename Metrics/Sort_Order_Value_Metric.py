#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Sort_Order_Value_Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from . import Metric
import Metrics.Metric

class Sort_Order_Value_Metric(Metric.Metric):
    """
    Averages values encountered
    """

    def __init__(self, field_profile):
        """
        Constructor for the Sort_Order_Value_Metric class
        """
        Metric.Metric.__init__(self, field_profile)

        self.value              = None
        self.last_defined_value = None

    def analyse(self, field_value):
        """
        """
        # Cant determine sort order of null so ignore
        if field_value.actual == None:
            return

        # We havent determined a sort order yet
        if self.value == None:

            # If we've seen nothing but nulls up to now then dont update value
            if self.last_defined_value != None:

                if   field_value.actual < self.last_defined_value: self.value = "descending"
                elif field_value.actual > self.last_defined_value: self.value = "ascending"

        else:

            # We've already determined a sort order, if it looks any different then its random
            if self.value == "ascending":

                if field_value.actual < self.last_defined_value: self.value = "random"

            else:

                if field_value.actual > self.last_defined_value: self.value = "random"


        # Save last value
        self.last_defined_value = field_value.actual

    def get_result(self):
        """
        """
        return self.value


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
