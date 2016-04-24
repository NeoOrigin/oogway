#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Profiler
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     06/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

from Profiles.FieldProfile import *

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class Profiler:
    """
    A basic data profiler
    """

    def __init__(self, sample_size = 100, limit = 5, quick = False):
        """
        The Constructor for the Profiler class

        quick       - Determines the thoroughness of the profiling
        limit       - Sets the maximum number of values to display for multivalue metrics
        sample_size - Sets the percentage of records to sample during profiling
        """
        self.quick       = quick
        self.limit       = limit
        self.sample_size = sample_size

        self.reset()

    def set_field_names(self, fieldnames):
        """
        Sets the field names used to describe each individual field
        """

        self.fieldNames = fieldnames

    def set_null_values(self, null_values):
        """
        Sets the values to interpret as null for any given field
        """

        self.nullValues = null_values

    def set_default_values(self, default_values):
        """
        Sets the values to override with a default value if any were found to be null
        """

        self.defaultValues = default_values

    def reset(self):
        """
        Reset all saved metrics readdy for another run
        """

        # These metrics are updated on each record
        self.fields        = []
        self.fieldNames    = []
        self.nullValues    = []
        self.defaultValues = []

        self.num_fields = 0
        self.last_rec   = None

    def __add_field(self):
        """
        Call when a new field is found for the first time
        """
        p = FieldProfile()

        if self.num_fields < len( self.fieldNames    ): p.name          = self.fieldNames[    self.num_fields ]
        if self.num_fields < len( self.nullValues    ): p.null_value    = self.nullValues[    self.num_fields ]
        if self.num_fields < len( self.defaultValues ): p.default_value = self.defaultValues[ self.num_fields ]

        self.fields.append( p )

        self.num_fields += 1

    def add_record(self, rec):
        """
        Adds a record to be profiled
        """

        for field_num, value in enumerate( rec ):

            # Check if this is the first time we have seen this field, if so resize the arrays
            if field_num >= self.num_fields:
                self.__add_field()

            field = self.fields[ field_num ]

            field.profile( value )

        # Save off the last fow we can use later for comparison
        self.last_rec = rec

    def finalize(self):
        """
        Called after all records have been profiled to finalize metrics that provide summation results
        """
        for field in self.fields:
            field.finalize()

    def get_results_dictionary(self):
        """
        Returns the metrics calculated by this Profiler as a large data table (list within dict)
        """

        data  = {}
        table = self.get_results_table()

        # Create a dictionary where the first coloumn now represents our dictionary keys
        for row in table:
            data[ row[0] ] = row[1:]

        return table

    def get_results_table(self):
        """
        Returns the metrics calculated by this Profiler as a large data table (list within list)
        """
        fieldNames       = []
        formatType       = []
        subFormatType    = []
        sortOrder        = []
        percent_nulls    = []
        percent_defined  = []
        percent_unique   = []
        valueCount       = []
        nullCount        = []
        definedCount     = []
        blankCount       = []
        defaultCount     = []
        distinctCount    = []
        uniqueCount      = []
        distinctDefined  = []
        widestDefined    = []
        narrowestDefined = []
        maxValues        = []
        minValues        = []
        sumValues        = []
        avgValues        = []
        avgDefined       = []
        modalValues      = []
        modalDefined     = []

        for field in self.fields:
            count = field.metrics[ "Total Count" ].get_result()

            fieldNames.append(       field.name                   )
            #formatType.append(       field.format_type            )
            #subFormatType.append(    field.sub_format_type        )
            sortOrder.append(        field.metrics[ "Sort Order"      ].get_result()             )
            #percent_nulls.append(    field.percent_null           )
            #percent_defined.append(  field.percent_defined        )
            #percent_unique.append(   field.percent_unique         )
            valueCount.append(       count            )
            nullCount.append(        field.metrics[ "Null Count"      ].get_result()             )
            definedCount.append(     field.metrics[ "Not Null Count"  ].get_result()             )
            blankCount.append(       field.metrics[ "Blank Count"     ].get_result()             )
            defaultCount.append(     field.metrics[ "Default Count"   ].get_result()             )
            #distinctCount.append(    field.distinct_count         )
            uniqueCount.append(      field.metrics[ "Unique Values"   ].get_result().count()             )
            #distinctDefined.append(  field.distinct_defined_count )
            #widestDefined.append(    field.max_length_value       )
            #narrowestDefined.append( field.min_length_value       )
            maxValues.append(        field.metrics[ "Max Values"      ].get_result()              )
            minValues.append(        field.metrics[ "Min Values"      ].get_result()              )
            sumValues.append(        field.metrics[ "Total Sum"       ].get_result()              )
            avgValues.append(        field.metrics[ "Total Sum"       ].get_average( count )              )
            #avgDefined.append(       field.avg_defined            )
            #modalValues.append(      field.modal_value            )
            #modalDefined.append(     field.modal_defined          )

        data = []
        data.append( [ "Field Names"             ] + fieldNames                )         # Output the fields we have found
        #data.append( [ "Data Types"              ] + formatType                )         # The types of the fields we have found
        #data.append( [ "Data Format"             ] + subFormatType             )
        data.append( [ "Sort Order"              ] + sortOrder                 )         # The order of the fields values
        #data.append( [ "Percentage Nulls"        ] + percent_nulls             )         # Percent of nulls compared to input we have found
        #data.append( [ "Percentage Defined"      ] + percent_defined           )         # Percent of defined compared to input we have found
        #data.append( [ "Percentage Unique"       ] + percent_unique            )         # Percent of unique values compared to input we have found
        data.append( [ "Count"                   ] + valueCount                )         # No. of rows found for each field
        data.append( [ "Null Count"              ] + nullCount                 )         # No. of nulls found in each field
        data.append( [ "Not Null Count"          ] + definedCount              )         # No. of non nulls found in each field
        data.append( [ "Blank Count"             ] + blankCount                )         # No. of blanks found in each field
        data.append( [ "Default Count"           ] + defaultCount              )         # No. of default values found in each field
        #data.append( [ "Distinct Count"          ] + distinctCount             )
        data.append( [ "Unique Count"            ] + uniqueCount               )
        #data.append( [ "Distinct Not Null Count" ] + distinctDefined           )
        #data.append( [ "Max Length Values"       ] + widestDefined             )
        #data.append( [ "Min Length Values"       ] + narrowestDefined          )
        data.append( [ "Max Values"              ] + maxValues                 )
        data.append( [ "Min Values"              ] + minValues                 )
        data.append( [ "Sum Values"              ] + sumValues                 )
        data.append( [ "Avg Values"              ] + avgValues                 )
        #data.append( [ "Avg Not Null Values"     ] + avgDefined                )
        #data.append( [ "Mean Values"             ] + modalValues               )
        #data.append( [ "Mean Not Null Values"    ] + modalDefined              )

        return data

    def __str__(self):
        """
        Outputs the relevant metrics in a basic newline delimited list
        """

        return     "-- Info -----------------------------------------------------"                 \
               + "\nField Names             = " + repr( self.m_fieldNames                        ) \
               + "\nPercentage Nulls        = " + repr( self.m_finalize_percentNulls             ) \
               + "\nPercentage Unique       = " + repr( self.m_finalize_percentUnique            ) \
               + "\n-- Counts ---------------------------------------------------"                 \
               + "\nCount                   = " + repr( self.m_valueCount                        ) \
               + "\nNull Count              = " + repr( self.m_nullCount                         ) \
               + "\nNot Null Count          = " + repr( self.m_definedCount                      ) \
               + "\nBlank Count             = " + repr( self.m_blankCount                        ) \
               + "\nDefault Count           = " + repr( self.m_defaultCount                      ) \
               + "\nDistinct Count          = " + repr( self.m_finalize_distinctCount            ) \
               + "\nDistinct Not Null Count = " + repr( self.m_finalize_distinctDefined          ) \
               + "\nUnique Count            = " + repr( self.m_finalize_uniqueCount              ) \
               + "\n-- Values ---------------------------------------------------"                 \
               + "\nData Types              = " + repr( self.m_formatType                        ) \
               + "\nData Format             = " + repr( self.m_subFormatType                     ) \
               + "\nSort Order              = " + repr( self.m_sortOrder                         ) \
               + "\nMax Length Values       = " + repr( self.m_finalize_widestDefined            ) \
               + "\nMin Length Values       = " + repr( self.m_finalize_narrowestDefined         ) \
               + "\nMax Values              = " + repr( self.m_maxValues                         ) \
               + "\nMin Values              = " + repr( self.m_minValues                         ) \
               + "\nSum Values              = " + repr( self.m_sumValues                         ) \
               + "\nAvg Values              = " + repr( self.m_finalize_avgValues                ) \
               + "\nAvg Not Null Values     = " + repr( self.m_finalize_avgDefined               ) \
               + "\nMean Values             = " + repr( self.m_finalize_modalValues              ) \
               + "\nMean Not Null Values    = " + repr( self.m_finalize_modalDefined             );


if __name__ == '__main__':
    pass
