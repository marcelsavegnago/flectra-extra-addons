.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======
Sentry
======

This module allows painless `Sentry <https://sentry.io/>`__ integration with
Flectra.

Installation
============

The module can be installed just like any other Flectra module, by adding the
module's directory to Flectra *addons_path*. In order for the module to correctly
wrap the Flectra WSGI application, it also needs to be loaded as a server-wide
module. This can be done with the ``server_wide_modules`` parameter in your
Flectra config file or with the ``--load`` command-line parameter.

This module additionally requires the raven_ Python package to be available on
the system. It can be installed using pip::

    pip install raven

Configuration
=============

The following additional configuration options can be added to your Flectra
configuration file:

=============================  ====================================================================  ================================================================
        Option                                          Description                                                         Default
=============================  ====================================================================  ================================================================
``sentry_dsn``                 Sentry *Data Source Name*. You can find this value in your Sentry     ``''``
                               project configuration. Typically it looks something like this:
                               *https://<public_key>:<secret_key>@sentry.example.com/<project id>*
                               This is the only required option in order to use the module.

``sentry_enabled``             Whether or not Sentry logging is enabled.                             ``False``

``sentry_logging_level``       The minimal logging level for which to send reports to Sentry.        ``warn``
                               Possible values: *notset*, *debug*, *info*, *warn*, *error*,
                               *critical*. It is recommended to have this set to at least *warn*,
                               to avoid spamming yourself with Sentry events.

``sentry_exclude_loggers``     A string of comma-separated logger names which should be excluded     ``werkzeug``
                               from Sentry.

``sentry_ignored_exceptions``  A string of comma-separated exceptions which should be ignored.       ``flectra.exceptions.AccessDenied,
                               You can use a star symbol (*) at the end, to ignore all exceptions    flectra.exceptions.AccessError,
                               from a module, eg.: *flectra.exceptions.**.                           flectra.exceptions.DeferredException,
                                                                                                     flectra.exceptions.MissingError,
                                                                                                     flectra.exceptions.RedirectWarning,
                                                                                                     flectra.exceptions.UserError,
                                                                                                     flectra.exceptions.ValidationError,
                                                                                                     flectra.exceptions.Warning,
                                                                                                     flectra.exceptions.except_orm``

``sentry_processors``          A string of comma-separated processor classes which will be applied   ``raven.processors.SanitizePasswordsProcessor,
                               on an event before sending it to Sentry.                              flectra.addons.sentry.logutils.SanitizeFlectraCookiesProcessor``

``sentry_transport``           Transport class which will be used to send events to Sentry.          ``threaded``
                               Possible values: *threaded*: spawns an async worker for processing
                               messages, *synchronous*: a synchronous blocking transport;
                               *requests_threaded*: an asynchronous transport using the *requests*
                               library; *requests_synchronous* - blocking transport using the
                               *requests* library.

``sentry_include_context``     If enabled, additional context data will be extracted from current    ``True``
                               HTTP request and user session (if available). This has no effect
                               for Cron jobs, as no request/session is available inside a Cron job.

``sentry_flectra_dir``         Absolute path to your Flectra installation directory.
                               This is optional and will only be used to extract the Flectra
                               Git commit, which will be sent to Sentry, to allow to distinguish
                               between Flectra updates.
=============================  ====================================================================  ================================================================

Other `client arguments
<https://docs.sentry.io/clients/python/advanced/#client-arguments>`_ can be
configured by prepending the argument name with *sentry_* in your Flectra config
file. Currently supported additional client arguments are: ``install_sys_hook,
include_paths, exclude_paths, machine, auto_log_stacks, capture_locals,
string_max_length, list_max_length, site, include_versions, environment``.

Example Flectra configuration
-----------------------------

Below is an example of Flectra configuration file with *Flectra Sentry* options::

    [options]
    sentry_dsn = https://<public_key>:<secret_key>@sentry.example.com/<project id>
    sentry_enabled = true
    sentry_logging_level = warn
    sentry_exclude_loggers = werkzeug
    sentry_ignore_exceptions = flectra.exceptions.AccessDenied,flectra.exceptions.AccessError,flectra.exceptions.MissingError,flectra.exceptions.RedirectWarning,flectra.exceptions.UserError,flectra.exceptions.ValidationError,flectra.exceptions.Warning,flectra.exceptions.except_orm
    sentry_processors = raven.processors.SanitizePasswordsProcessor,flectra.addons.sentry.logutils.SanitizeFlectraCookiesProcessor
    sentry_transport = threaded
    sentry_include_context = true
    sentry_environment = production
    sentry_auto_log_stacks = false
    sentry_flectra_dir = /home/flectra/flectra/

Usage
=====

Once configured and installed, the module will report any logging event at and
above the configured Sentry logging level, no additional actions are necessary.

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/149/10.0

Known issues / Roadmap
======================

* **No database separation** -- This module functions by intercepting all Flectra
  logging records in a running Flectra process. This means that once installed in
  one database, it will intercept and report errors for all Flectra databases,
  which are used on that Flectra server.

* **Frontend integration** -- In the future, it would be nice to add
  Flectra client-side error reporting to this module as well, by integrating
  `raven-js <https://github.com/getsentry/raven-js>`_. Additionally, `Sentry user
  feedback form <https://docs.sentry.io/learn/user-feedback/>`_ could be
  integrated into the Flectra client error dialog window to allow users shortly
  describe what they were doing when things went wrong.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/server-tools/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* `Module Icon <https://sentry.io/branding/>`_

Contributors
------------

* Mohammed Barsi <barsintod@gmail.com>
* Andrius Preimantas <andrius@versada.eu>
* Naglis Jonaitis <naglis@versada.eu>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.


.. _raven: https://github.com/getsentry/raven-python
