..  _api:

API
===

This is a description of the API classes. The python API closely follows the `C interface guide<https://aa.usno.navy.mil/software/novas/novas_c/NOVAS_C3.1_Guide.pdf>`_ but there are differences. For example the `accuracy`
parameter in many of the python functions has been moved to the end of the argument list so default values can be easily supplied.

Super Functions
^^^^^^^^^^^^^^^

app_planet
----------
.. autofunction :: novas.compat.app_planet

app_star
--------
.. autofunction :: novas.compat.app_star


astro_planet
------------
.. autofunction :: novas.compat.astro_planet

astro_star
----------
.. autofunction :: novas.compat.astro_star

cel2ter
-------
.. autofunction :: novas.compat.cel2ter

local_planet
------------
.. autofunction :: novas.compat.local_planet

local_star
----------
.. autofunction :: novas.compat.local_star


mean_star
---------
.. autofunction :: novas.compat.mean_star

place
-----
.. autofunction :: novas.compat.place

sidereal_time
-------------
.. autofunction :: novas.compat.sidereal_time

ter2cel
-------
.. autofunction :: novas.compat.ter2cel

topo_planet
-----------
.. autofunction :: novas.compat.topo_planet

topo_star
---------
.. autofunction :: novas.compat.topo_star

virtual_planet
--------------
.. autofunction :: novas.compat.virtual_planet

virtual_star
------------
.. autofunction :: novas.compat.virtual_star


Utility Functions
^^^^^^^^^^^^^^^^^

aberration
----------
.. autofunction :: novas.compat.aberration

bary2obs
--------
.. autofunction :: novas.compat.bary2obs

d_light
-------
.. autofunction :: novas.compat.d_light

equ2ecl
-------
.. autofunction :: novas.compat.equ2ecl

equ2ecl_vec
-----------
.. autofunction :: novas.compat.equ2ecl_vec

ecl2equ_vec
-----------
.. autofunction :: novas.compat.ecl2equ_vec

equ2gal
-------
.. autofunction :: novas.compat.equ2gal

equ2hor
-------
.. autofunction :: novas.compat.equ2hor

era
---
.. autofunction :: novas.compat.era

frame_tie
---------
.. autofunction :: novas.compat.frame_tie

gcrs2equ
--------
.. autofunction :: novas.compat.gcrs2equ

geo_posvel
----------
.. autofunction :: novas.compat.geo_posvel

grav_def
--------
.. autofunction :: novas.compat.grav_def

grav_vec
--------
.. autofunction :: novas.compat.grav_vec

light_time
----------
.. autofunction :: novas.compat.light_time

limb_angle
----------
.. autofunction :: novas.compat.limb_angle

nutation
--------
.. autofunction :: novas.compat.nutation

precession
----------
.. autofunction :: novas.compat.precession

proper_motion
-------------
.. autofunction :: novas.compat.proper_motion

rad_vel
-------
.. autofunction :: novas.compat.rad_vel

radec2vector
------------
.. autofunction :: novas.compat.radec2vector

spin
----
.. autofunction :: novas.compat.spin

starvectors
-----------
.. autofunction :: novas.compat.starvectors

terra
-----
.. autofunction :: novas.compat.terra
cel_pole
--------
.. autofunction :: novas.compat.cel_pole

vector2radec
------------
.. autofunction :: novas.compat.vector2radec

wobble
------
.. autofunction :: novas.compat.wobble

Basic Functions
^^^^^^^^^^^^^^^
The Basic functions defined in the NOVAS C3.1 guide

cal_date
--------
.. autofunction :: novas.compat.cal_date

cio_array
---------
This function is not yet supported in novas_py

cio_basis
---------
.. autofunction :: novas.compat.cio_basis

cio_location
------------
.. autofunction :: novas.compat.cio_location

cio_ra
------
.. autofunction :: novas.compat.cio_ra

e_tilt
------
.. autofunction :: novas.compat.e_tilt

ee_ct
-----
.. autofunction :: novas.compat.ee_ct

ephemeris
---------
.. autofunction :: novas.compat.ephemeris

iau2000a
--------
.. autofunction :: novas.compat.nutation.iau2000a

iau2000b
--------
.. autofunction :: novas.compat.nutation.iau2000b

ira_equinox
------------
.. autofunction :: novas.compat.ira_equinox

julian_date
-----------
.. autofunction :: novas.compat.julian_date

norm_ang
--------
.. autofunction :: novas.compat.norm_ang

nu2000k
-------
.. autofunction :: novas.compat.nutation.nu2000k

mean_obliq
-----------
.. autofunction :: novas.compat.mean_obliq

nutation_angles
---------------
.. autofunction :: novas.compat.nutation_angles

refract
-------
.. autofunction :: novas.compat.refract

tdb2tt
------
.. autofunction :: novas.compat.tdb2tt

Miscellaneous Functions
^^^^^^^^^^^^^^^^^^^^^^^

ephem_open
----------
.. autofunction :: novas.compat.eph_manager.ephem_open

ephem_close
-----------
.. autofunction :: novas.compat.eph_manager.ephem_close

fund_args
---------
.. autofunction :: novas.compat.fund_args

make_cat_entry
--------------
.. autofunction :: novas.compat.make_cat_entry

make_in_space
-------------
.. autofunction :: novas.compat.make_in_space

make_object
-----------
.. autofunction :: novas.compat.make_object

make_observer
-------------
.. autofunction :: novas.compat.make_observer

make_observer_at_geocenter
--------------------------
.. autofunction :: novas.compat.make_observer_at_geocenter

make_observer_on_surface
------------------------
.. autofunction :: novas.compat.make_observer_on_surface

make_observer_in_space
----------------------
.. autofunction :: novas.compat.make_observer_in_space

make_on_surface
---------------
.. autofunction :: novas.compat.make_on_surface

planet_ephemeris
----------------
.. autofunction :: novas.compat.eph_manager.planet_ephemeris

solarsystem
-----------
.. autofunction :: novas.compat.solsys.solarsystem

split
-----
.. autofunction :: novas.compat.eph_manager.split

state
-----
.. autofunction :: novas.compat.eph_manager.state

transform_cat
-------------
.. autofunction :: novas.compat.transform_cat

transform_hip
-------------
.. autofunction :: novas.compat.transform_hip

