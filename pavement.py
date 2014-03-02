from paver.easy import *
import paver.doctools
from paver.setuputils import setup

options(
    setup=dict(
        name='ffmpegwrapper',
        version='0.1-dev',
        packages=['ffmpegwrapper'],
        author='Tobias Reese',
        author_email='tobias.reese@gmail.com',
        url='http://github.com/interrupted/ffmpegwrapper',
        description='A simple wrapper for ffmpeg-cli',
        keywords='Video Convert Ffmpeg',
        long_description=__doc__,
        license='BSD',
        test_suite='test',
        tests_require='mock>=0.7.2',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Topic :: Multimedia :: Video',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    ),

    sphinx=Bunch(
        builddir="build"
    )
)

@task
def doc_clean():
    """Make sure clean does not delete anything"""
    pass


