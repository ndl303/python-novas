# -*- coding: utf-8 -*-

import os
import os.path
import sys
import glob
from ctypes import CDLL

# Exception strings used when checking inputs
_neg_err = "{name} must be >= 0.0"
_hour_range_err = "{name} must be in the range 0.0 <= {name} < 24.0"
_elev_range_err = "{name} must be in the range -90.0 <= {name} <= 90.0"
_az180_range_err = "{name} must be in the range -180.0 <= {name} <= 180.0"
_az360_range_err = "{name} must be in the range 0.0 <= {name} <= 360.0"
_vector_len_err = "{name} must be a sequence of length 3"
_option_err = "{name} must be in {allowed}"
_jd_year_err = "{name} must be >= -4712"
_month_range_err = "{name} must be 1 <= {name} <= 12"
_day_range_err = "{name} must be 1 <= {name} <= {daysinmonth}"

_days_in_month = (None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


class NonConvergentError(Exception):
    pass


class IndeterminateError(Exception):
    pass


class InitializationError(Exception):
    pass


def _check_c_errors(retval, func, args):
    """
    Function to check return values from wrapped C functions.

    This function is used in conjunction with the ctypes ``errcheck`` attribute
    attached to a C function object. Assigning this function to the
    ``errcheck`` attribute causes an automatic check of the return value from
    the C function. Every C function object that utilizes this ``errcheck``
    feature must also have an attribute called ``c_errors`` assigned to it.
    ``c_errors`` is a dictionary where the keys are possible return values and
    the values are length-2 tuples; each tuple consists of the exception to be
    raised and the message sent to that exception.

    https://docs.python.org/3.4/library/ctypes.html#ctypes._FuncPtr.errcheck

    """
    if retval:
        error = func.c_errors[retval]
        raise error[0](error[1])


def get_and_configure_library():
    dirname = os.path.dirname(__file__)
    names = glob.glob( os.path.join(dirname,'libnovas.*') )
    libnovas = None
    if (names is not None) and (len(names) > 0):
        dllname = names[0]
        path_to_libnovas = dllname
        if os.path.isfile(path_to_libnovas):
            libnovas = CDLL(path_to_libnovas)
    else:
        print('Could not find the libnovas DLL or shared object in folder {}. Thats usually a problem although it is ok if you are just building Sphinx documentation)'.format(dirname))

    return libnovas

#------------------------------------------------------------------------------
#           check_ephemeris_file
#------------------------------------------------------------------------------

def _check_ephemeris_file()->str:
    ephem_file = None
    ephemeris_spec = os.path.join(os.path.dirname(__file__), 'ephemeris_data', '*.bin')
    files = glob.glob(ephemeris_spec)
    if len(files) > 0:
        ephem_file = files[0]
    else:
        print('Did not find any ephemeris files. Creating the ephemerides')
        from . asc2eph  import create_ephemeris
        create_ephemeris()
        files = glob.glob(ephemeris_spec)
        ephem_file = files[0]
    return ephem_file

#------------------------------------------------------------------------------
#           default_ephemeris_file
#------------------------------------------------------------------------------

def default_ephemeris_file():
    return _check_ephemeris_file()


novaslib  = get_and_configure_library()


