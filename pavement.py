from os.path import exists, join
from paver.doctools import _get_paths
from paver.easy import *
import paver.doctools
from paver.setuputils import setup

setup(
        name='ffmpegwrapper',
        version='0.1-dev',
        packages=['ffmpegwrapper'],
        test_suite='test',
        tests_require='mock>=0.7.2',
        author='Tobias Reese',
        author_email='tobias.reese@gmail.com',
        url='http://github.com/interrupted/ffmpegwrapper',
        description='A simple wrapper for ffmpeg-cli',
        keywords='Video Convert Ffmpeg',
        long_description=__doc__,
        license='BSD',
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
)


options(
    sphinx=Bunch(
        builddir="build"
    )
)


@task
def doc_clean():
    """Make sure clean does not delete anything"""
    pass

@task
def prepare_doc_dir():
    """Make sure doc dir is correctly initialized."""
    options.order('sphinx', add_rest=True)
    paths = _get_paths()
    paths.builddir
    if not exists(join(paths.builddir, "html", ".git")):
        sh('git submodule update --init --recursive')

@task
@needs('prepare_doc_dir', 'paver.doctools.html')
def html():
    pass


