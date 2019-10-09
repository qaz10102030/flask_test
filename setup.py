import os
import re

from setuptools import setup

install_requires = ["flask==1.1.1", "requests==2.22.0"]
dev_requires = ["black==19.3b0", "isort==4.3.21", "pylint==2.4.2"]
test_requires = [
    "coverage==4.5.3",
    "pytest==4.6.2",
    "pytest-cov==2.7.1",
    "pytest-html==1.20.0",
    "pytest-runner==5.1",
    "tox==3.12.1",
]

package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "flask_test")
init_path = os.path.join(package_path, "__init__.py")
with open(init_path, "r") as f:
    version = re.findall(r"^__version__ = \"([^']+)\"\r?$", f.read(), re.M)[0]

setup(
    name="flask-test",
    version=version,
    packages=["flask_test"],
    install_requires=install_requires,
    extras_require={"dev": dev_requires + test_requires, "test": test_requires},
)
