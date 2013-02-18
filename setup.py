from setuptools import setup, find_packages
setup(
    name="skeletool",
    version="0.3",
    packages=find_packages(),

    # Dependencies
    install_requires=[],

    package_data={
        '': ['COPYING', "*.txt"],
    },

    entry_points={
        'console_scripts': [
            'skeletool=skeletool.skeletool:run',
        ],
    },

    # Metadata
    author='Fabien Bouleau',
    author_email='fabien.bouleau@gmail.com',
    description='Framework package for integrated command-line development',
    license='GPLv3',
    keywords='framework command-line API',
    url='',
)
