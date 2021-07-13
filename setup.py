from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('posii/scripts/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name="posii",
    version=main_ns['__version__'],
    author="Tom Stanton",
    author_email="tomdstanton@gmail.com",
    description="Position Interrogator",
    url="https://github.com/tomdstanton/posii",
    project_urls={
        "Bug Tracker": "https://github.com/tomdstanton/posii/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bioinformatics",
        "Operating System :: POSIX :: Linux"],
    packages=find_packages(),
    python_requires=">=3.7",
    scripts=['src/posii'],
    keywords='bioinformatics',
    zip_safe=False,
)
