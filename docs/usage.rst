=====
Usage
=====

To use django-recaptcha-utils in a project, add it to your `INSTALLED_APPS`:

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
