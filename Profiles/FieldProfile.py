#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        FieldProfile
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     12/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

from Metrics.Blank_Count_Metric       import *
from Metrics.Default_Count_Metric     import *
from Metrics.Distinct_Values_Metric   import *
from Metrics.Max_Values_Metric        import *
from Metrics.Max_Length_Values_Metric import *
from Metrics.Min_Values_Metric        import *
from Metrics.Min_Length_Values_Metric import *
from Metrics.Negative_Count_Metric    import *
from Metrics.Not_Null_Count_Metric    import *
from Metrics.Null_Count_Metric        import *
from Metrics.Positive_Count_Metric    import *
from Metrics.Sort_Order_Value_Metric  import *
from Metrics.Total_Count_Metric       import *
from Metrics.Total_Sum_Metric         import *
from Metrics.Unique_Values_Metric     import *
from Metrics.Zero_Count_Metric        import *

from Profiles.Field_Value import *
from Profiles.Tracker     import *

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class FieldProfile:
    """
    Handles the data profiling for a single field
    """

    def __init__(self, name = None, null_value = None, default_value = None, limit = 5 ):
        """
        """

        self.__not_applicable__  = "-"               # Holds the N/A value if the type does not support that metric
        self.__value_seperator__ = ","               # Holds the value used to separate elements in multivalued metrics
        self.__count_seperator__ = ":"               # Holds the value used to separate the count in multivalued metrics

        self.name          = name                    # Holds the name of this field
        self.null_value    = null_value              # Holds the value used to interpret this field as null
        self.default_value = default_value           # Holds the default value to replace with if the value is null
        self.display_limit = limit                   # Holds the limit of the number of items to display for multi valued items
        self.curr_value    = None                    # Holds the current value this field was profiled with
        self.last_value    = None                    # Holds the last value this field was profiled with

        # For performance reasons hold the metrics in 2 forms, one as a list the other as a named dictionary which is easier for the
        # user to query against
        self.__metrics = []; self.metrics = {}
        self.__metrics.append( Total_Count_Metric(       self ) ); self.metrics[ "Total Count"           ] = self.__metrics[-1]
        self.__metrics.append( Null_Count_Metric(        self ) ); self.metrics[ "Null Count"            ] = self.__metrics[-1]
        self.__metrics.append( Not_Null_Count_Metric(    self ) ); self.metrics[ "Not Null Count"        ] = self.__metrics[-1]
        self.__metrics.append( Blank_Count_Metric(       self ) ); self.metrics[ "Blank Count"           ] = self.__metrics[-1]
        self.__metrics.append( Zero_Count_Metric(        self ) ); self.metrics[ "Zero Count"            ] = self.__metrics[-1]
        self.__metrics.append( Default_Count_Metric(     self ) ); self.metrics[ "Default Count"         ] = self.__metrics[-1]
        self.__metrics.append( Negative_Count_Metric(    self ) ); self.metrics[ "Negative Count"        ] = self.__metrics[-1]
        self.__metrics.append( Positive_Count_Metric(    self ) ); self.metrics[ "Positive Count"        ] = self.__metrics[-1]
        self.__metrics.append( Distinct_Values_Metric(   self ) ); self.metrics[ "Distinct Values"       ] = self.__metrics[-1]
        self.__metrics.append( Unique_Values_Metric(     self ) ); self.metrics[ "Unique Values"         ] = self.__metrics[-1]
        self.__metrics.append( Total_Sum_Metric(         self ) ); self.metrics[ "Total Sum"             ] = self.__metrics[-1]
        self.__metrics.append( Max_Values_Metric(        self ) ); self.metrics[ "Max Values"            ] = self.__metrics[-1]
        self.__metrics.append( Min_Values_Metric(        self ) ); self.metrics[ "Min Values"            ] = self.__metrics[-1]
        self.__metrics.append( Max_Length_Values_Metric( self ) ); self.metrics[ "Max Length Values"     ] = self.__metrics[-1]
        self.__metrics.append( Min_Length_Values_Metric( self ) ); self.metrics[ "Min Length Values"     ] = self.__metrics[-1]
        self.__metrics.append( Sort_Order_Value_Metric(  self ) ); self.metrics[ "Sort Order"            ] = self.__metrics[-1]

        # Init our metrics
        for metric in self.__metrics:
            metric.initialize()

    def get_type( self, value ):
        """
        Helper function that determines the format of a field and a native format
        value useful for later comparison checks etc
        """

        field_format        = "undefined"
        field_subformat     = ""
        field_value         = value
        field_value_default = value

        if value == self.null_value:

            field_value = None

            # If there are defaults to swap
            if self.default_value != None:
                field_value_default = self.default_value

        else:

            # If it look like a number first see if its a datetime, note that this function
            # does not handle negative numbers just pure digits
            if value.isdigit():

                try:
                    field_value  = datetime.strptime( value, "%Y%m%d" )

                    if field_value.strftime( "%Y%m%d" ) != value:
                        field_format = "integer"
                    else:
                        field_format = "datetime"

                    field_value = int(value)

                except:
                    try:
                        field_value  = datetime.strptime( value, "%Y%m%d%H%M%S" )
                        if field_value.strftime( "%Y%m%d%H%M%S" ) != value:
                            field_format = "integer"
                        else:
                            field_format = "datetime"
                        field_value = int(value)
                    except:
                        try:
                            field_format = "integer"
                            field_value  = int(value)
                        except:
                            field_format = "long"
                            field_value   = long(value)
                        field_subformat = "unsigned"

            else:
                try:
                    field_value     = int(value)
                    field_format    = "integer"
                    field_subformat = "signed"
                except:
                    try:
                        field_value     = long(value)
                        field_format    = "long"
                        field_subformat = "signed"
                    except:
                        try:
                            field_value  = float(value)
                            field_format = "numeric"
                        except:
                            try:
                                field_value  = complex(value)
                                field_format = "complex"
                            except:
                                if value.lower() == "true" or value.lower() == "false":
                                    field_value  = bool(value)
                                    field_format = "boolean"
                                else:
                                    try:
                                        field_value     = datetime.strptime( value, "%Y-%m-%d" )
                                        field_format    = "datetime"
                                        field_subformat = "string"
                                    except:
                                        try:
                                            field_value    = datetime.strptime( value, "%Y.%m.%d" )
                                            field_format   = "datetime"
                                            field_subformat = "string"
                                        except:
                                            try:
                                                field_value  = datetime.strptime( value, "%d/%m/%Y" )
                                                field_format = "datetime"
                                                field_subformat = "string"
                                            except:
                                                try:
                                                    field_value  = datetime.strptime( value, "%m/%d/%Y" )
                                                    field_format = "datetime"
                                                    field_subformat = "string"
                                                except:
                                                    try:
                                                        field_value  = datetime.strptime( value, "%Y-%m-%d %H:%M:%S" )
                                                        field_format = "datetime"
                                                        field_subformat = "string"
                                                    except:
                                                        field_format = "string"
                                                        field_value  = value

            field_value_default = field_value

        return field_format, field_subformat, field_value, field_value_default

    def __set_format(self, field_value):
        """
        Sets the format of the field based on the current value looking back over the previous values
        """

        field_format    = field_value.format
        field_subformat = field_value.subformat

        current_format    = self.format_type
        current_subformat = self.sub_format_type

        # No point continuing as no change here
        if     field_format    == current_format   \
           and field_subformat == current_subformat:
            return

        # Cant upgrade from a string so return
        # Never upgrade to an undefined value
        if field_format == "undefined" or current_format == "string":
            return


        # A string is the highest you can go so automatically set it with no checks
        # also set if undefined
        if current_format == "undefined" or field_format == "string":

            # undefined -> boolean, integer, long, numeric, complex, datetime, string

            self.format_type     = field_format
            self.sub_format_type = field_subformat
            return


        # Somethings changed !!!!!!!!!!!!!!!

        if current_format == "boolean":

            # boolean -> string
            # integer, long, numeric, complex, datetime !-> boolean

            self.format_type     = "string"
            self.sub_format_type = ""

        elif current_format == "integer":

            # integer -> long, numeric, complex, string, datetime(int)
            # boolean, string, datetime(string), numeric, complex !-> integer

            if field_format == "boolean":
                field_format    = "string"
                field_subformat = ""
            elif     field_format    == "datetime" \
                 and field_subformat == "string":
                field_format    = "string"
                field_subformat = ""

            self.format_type     = field_format
            self.sub_format_type = field_subformat

        elif current_format == "long":

            # long -> numeric, complex, string
            # boolean, string, datetime, numeric, complex !-> long

            if field_format == "boolean":
                field_format    = "string"
                field_subformat = ""
            elif     field_format    == "datetime" \
                 and field_subformat == "string":
                field_format    = "string"
                field_subformat = ""
            elif field_format == "integer":
                return

            self.format_type     = field_format
            self.sub_format_type = field_subformat

        elif current_format == "numeric":

            # numeric -> complex, string
            # boolean, string, datetime, complex !-> numeric

            if field_format == "boolean":
                field_format    = "string"
                field_subformat = ""
            elif     field_format    == "datetime" \
                 and field_subformat == "string":
                field_format    = "string"
                field_subformat = ""
            elif field_format == "integer" or field_format == "long":
                return

            self.format_type     = field_format
            self.sub_format_type = field_subformat

        elif current_format == "complex":

            if field_format == "boolean":
                field_format    = "string"
                field_subformat = ""
            elif     field_format    == "datetime" \
                 and field_subformat == "string":
                field_format    = "string"
                field_subformat = ""
            elif field_format == "integer" or field_format == "long" or field_format == "numeric":
                return

            self.format_type     = field_format
            self.sub_format_type = field_subformat

        elif current_format == "datetime":

            if field_format == "boolean":
                field_format    = "string"
                field_subformat = ""
            if field_subformat != "":
                pass
            else:
                pass

            if self.m_subFormatType[ field_num ] != "string":
                self.format_type     = field_format
                self.sub_format_type = field_subformat

    def finalize(self):
        """
        """
        pass

    def finalize_old(self):
        """
        Called when no more records are to be added, this performs the final summation on aggregated metrics
        """

        # Finalise our metrics
        for metric in self.__metrics:
            metric.finalize()

        self.modal_value       = self.__not_applicable__
        self.modal_defined     = self.__not_applicable__

        highest_count     = Counter()
        highest_defined   = Counter()
        widest_defined    = Counter()
        narrowest_defined = None

        distinctCount = self.distinct_values.count()
        for key in self.distinct_values.get_tracked_keys():

            val = self.distinct_values.get_value( key )

            if val > highest_count:
                highest_count = val
                self.modal_value = str( key ) + self.__count_seperator__ + str( val )
            elif val == highest_count and self.modal_value.count( self.__value_seperator__ ) < self.display_limit - 1:
                self.modal_value = str( key ) + self.__value_seperator__ + self.modal_value

            if ( key ):
                if val > highest_defined:
                    highest_defined = val
                    self.modal_defined = str( key ) + self.__count_seperator__ + str( val )
                elif val == highest_defined and self.modal_defined.count( self.__value_seperator__ ) < self.display_limit - 1:
                    self.modal_defined = str( key ) + self.__value_seperator__ + self.modal_defined

            val = key
            if ( isinstance( val, str ) ):
                val = len( val )
            else:
                val = len( str( val ) )

        # Average the field values, you cant do this if its a string, boolean or undefined
        if self.format_type != "string" and self.format_type != "boolean" and self.format_type != "undefined":
            self.avg_values  = self.sum_value.get_average( self.value_count,   2 )
            self.avg_defined = self.sum_value.get_average( self.defined_count, 2 )

        # Calculate percentages based on total counts
        self.percent_null    = str( self.null_count.get_percentage(    self.value_count, 2 ) ) + "%"
        self.percent_defined = str( self.defined_count.get_percentage( self.value_count, 2 ) ) + "%"
        self.percent_unique  = str( self.unique_count.get_percentage(  self.value_count, 2 ) ) + "%"

        # Get a count of adistinct values
        self.distinct_count         = Counter( distinctCount )
        self.distinct_defined_count = Counter( distinctCount )

        # for distinct defined values remove any nulls from calculation
        if self.null_count > 0:
           self.distinct_defined_count.decrement()


    def profile(self, value):
        """
        Profile a value occurence for this field
        """

        # Then extract the interpreted value
        field_format, field_subformat, field_interpreted, field_value_default = self.get_type( value )
        field_value = Field_Value( value, field_interpreted           \
                                        , format    = field_format    \
                                        , subformat = field_subformat \
                                        , default   = field_value_default )

        self.curr_value = field_value

        # Analyse the field against each of our metrics
        for metric in self.__metrics:
            metric.analyse( field_value )

        # Save off the last fow we can use later for comparison
        self.last_value = field_value

def main():
    """
    """
    pass

if __name__ == '__main__':
    main()
