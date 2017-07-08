=============================
django-recaptcha-utils
=============================

.. image:: https://badge.fury.io/py/django-recaptcha-utils.svg
    :target: https://badge.fury.io/py/django-recaptcha-utils

.. image:: https://travis-ci.org/bulya/django-recaptcha-utils.svg?branch=master
    :target: https://travis-ci.org/bulya/django-recaptcha-utils

.. image:: https://codecov.io/gh/bulya/django-recaptcha-utils/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/bulya/django-recaptcha-utils

Extension for django-recaptcha

Documentation
-------------

The full documentation is at https://django-recaptcha-utils.readthedocs.io.

Quickstart
----------

Install django-recaptcha-utils::

    pip install django-recaptcha-utils

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'recaptcha_utils.apps.RecaptchaUtilsConfig',
        ...
    )

Add django-recaptcha-utils's URL patterns:

.. code-block:: python

    from recaptcha_utils import urls as recaptcha_utils_urls


    urlpatterns = [
        ...
        url(r'^', include(recaptcha_utils_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
