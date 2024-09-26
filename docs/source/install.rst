Installing Seabird
==================

Virtual Environments
--------------------

You don't need to, but I strongly recommend to use `virtualenv <https://virtualenv.pypa.io/en/stable/>`_ or `conda <https://conda.io/en/latest/>`_.

Using pip
---------

Currently, the most convenient way to install is with pip, by running in the terminal::

    pip install seabird

If you don't have pip installed, you'll need to `install pip <https://pip.pypa.io>`_ first.

Alternative
-----------

To install with netCDF support::

    pip install seabird[CDF]

To install with Quality Control support::

    pip install seabird[QC]
