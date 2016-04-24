#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        FieldFormat
# Purpose:
#
# Author:      Philip Bowditch
#
# Created:     13/03/2012
# Copyright:   (c) Philip Bowditch 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

__author__ = "Philip Bowditch"

# If present, use psyco to accelerate the program
try:    import psyco ; psyco.jit()
except: pass

class FieldFormat:
    """
    """
    def __init__(self):
        """
        """
        self.base_type      = None
        self.signed         = None
        self.endianess      = None
        self.representation = []

    def inspect_float(self, value):
        """
        """
        pass

    def inspect_string(self, value):
        """
        """
        pass

    def inspect_int(self, raw):
        """
        """
        self.base_type = "integer"
        self.signed    = self.signed or int(raw) < 0

        rep = ""
        for ch in raw:
            if ch >=0 and ch <= 9:
                rep += "[0-9]"
            else:
                rep += ch

        if rep not in self.representation:
            self.representation.append( rep )

    def inspect_long(self, raw):
        """
        """
        self.base_type = "long"
        self.signed    = self.signed or long( value ) < 0

        rep = ""
        for ch in raw:
            if ch >=0 and ch <= 9:
                rep += "[0-9]"
            else:
                rep += ch

        if rep not in self.representation:
            self.representation.append( rep )

    def inspect_boolean(self, value):
        """
        """
        self.base_type  = "boolean"
        self.signed     = False

        rep = ""
        for ch in raw:
            if ch >=0 and ch <= 9:
                rep += "[0-9]"
            elif ch >= "a" and ch <= "z":
                rep += "[a-z]"
            elif ch >= "A" and ch <= "Z":
                rep += "[A-Z]"
            else:
                rep += ch

        if rep not in self.representation:
            self.representation.append( rep )

    def inspect_datetime(self, value):
        """
        """
        pass

    def inspect( self, value ):
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

            # If it look like a number first see if its a datetime
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

def main():
    pass

if __name__ == '__main__':
    main()
