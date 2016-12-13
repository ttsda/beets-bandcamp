from setuptools import setup

setup(
    name='beets-bandcamp',
    version='0.1.0a1',
    description='Plugin for beets (http://beets.io) to use bandcamp as an autotagger source.',
    url='https://github.com/ttsda/beets-bandcamp',
    license='MIT',
    platforms='ALL',

    packages=['beetsplug'],

    install_requires=[
        'beets>=1.3.7',
        'requests',
        'beautifulsoup4',
        'isodate'
    ],

    classifiers=[
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
