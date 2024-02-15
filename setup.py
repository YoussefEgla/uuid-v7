"""Python setup.py for uuid_v7 package"""

import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("uuid_v7", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="uuid_v7",
    version=read("uuid_v7", "VERSION"),
    description="UUID v6 and v7 for Python 3.10+.",
    url="https://github.com/YoussefEgla/uuid-v7/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="YoussefEgla",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={"console_scripts": ["uuid_v7 = uuid_v7.__main__:main"]},
    extras_require={"test": read_requirements("requirements-test.txt")},
    python_requires=">=3.10",
)
