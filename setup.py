"""Setup configuration for the automation lab."""
from setuptools import setup, find_packages

setup(
    name="automation-lab",
    version="1.0.0",
    description="Python automation lab for pip, PyPI, and scripting",
    author="Student",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.4",
        ],
    },
    entry_points={
        "console_scripts": [
            "generate-log=lib.generate_log:generate_log",
        ],
    },
)
