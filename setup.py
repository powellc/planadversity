from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

version = __import__('planadversity').__version__

install_requires = [
    'setuptools',
    'Django==1.6.5',
    'django-configurations==0.8',
    'dj-database-url==0.3.0',
    'pylibmc==1.3.0',
    'boto==2.9.5',
    'South==1.0.0',
    'django-storages==1.1.8',
    'Pillow==2.5.1',
    'django-cache-url==0.8.0',
    'werkzeug==0.9.4',
    'gunicorn==0.17.4',
    'easy-thumbnails==1.2',
    'django-debug-toolbar==1.1',
    'django-extensions==1.3.4',
    'django-braces==1.4.0',
    'django-allauth==0.16.1',
    'django-floppyforms==1.1.1',
    'django-custom-user==0.4',
    'raven==5.0.0',
    'boto==2.9.5',
    'django-storages==1.1.8',
    'psycopg2==2.5',
    'Markdown>2.2.0',
    'django-sekizai>=0.7',
    'django-mptt==0.6.0',
    'django-bootstrap-form==3.1',
]


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

setup(
    name="planadversity",
    version=version,
    url='http://github.com/powellc/planadversity',
    license='BSD',
    platforms=['OS Independent'],
    description="An planadversity for django applications.",
    author="Colin Powell",
    author_email='colin.powell@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'planadversity': 'planadversity',
        'planadversity/templates': 'planadversity/templates',
    },
    entry_points={
        'console_scripts': [
            'planadversity = planadversity.manage_planadversity:main',
        ],
    },
)
