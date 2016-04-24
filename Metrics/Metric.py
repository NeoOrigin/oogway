#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Metric
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     17/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Metric:
    """
    """
    def __init__(self, field_profile):
        """
        """
        self.__not_applicable__  = "-"                # Holds the N/A value if the type does not support that metric
        self.__value_seperator__ = ","               # Holds the value used to separate elements in multivalued metrics
        self.__count_seperator__ = ":"               # Holds the value used to separate the count in multivalued metrics

        self.profile = field_profile

    def initialize(self):
        """
        """
        pass

    def analyse(self, field_value):
        """
        """
        pass

    def finalize(self):
        """
        """
        pass


def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
