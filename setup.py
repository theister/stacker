import os
from setuptools import setup, find_packages

VERSION = "2.0.0rc1"

src_dir = os.path.dirname(__file__)

def get_install_requirements(path):
    content = open(os.path.join(os.path.dirname(__file__), path)).read()
    return [req for req in content.split("\n") if req != "" and not req.startswith("#")]

install_requires = get_install_requirements("requirements.in")

setup_requires = ["pytest-runner"]

tests_require = get_install_requirements("test-requirements.in")

scripts = [
    "scripts/compare_env",
    "scripts/docker-stacker",
    "scripts/stacker.cmd",
    "scripts/stacker",
]


def read(filename):
    full_path = os.path.join(src_dir, filename)
    with open(full_path) as fd:
        return fd.read()


if __name__ == "__main__":
    setup(
        name="pinless-stacker",
        version=VERSION,
        author="Till Heistermann",
        author_email="theister@gmail.com",
        license="New BSD license",
        url="https://github.com/theister/pinless-stacker",
        description="AWS CloudFormation Stack manager",
        long_description=read("README.md"),
        packages=find_packages(),
        scripts=scripts,
        install_requires=install_requires,
        tests_require=tests_require,
        setup_requires=setup_requires,
        extras_require=dict(testing=tests_require),
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
        ],
    )
