import sys

from setuptools import setup

meta = dict(
    name="hepfab",
    version="0.1.0",
    description="Fabric for UW-HEP",
    author="Will Maier",
    author_email="wcmaier@hep.wisc.edu",
    packages=["hepfab"],
    test_suite="tests",
    install_requires=["setuptools"],
    keywords="fabric",
    #url="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
    ],
)

# Automatic conversion for Python 3 requires distribute.
if False and sys.version_info >= (3,):
    meta.update(dict(
        use_2to3=True,
    ))

setup(**meta)
