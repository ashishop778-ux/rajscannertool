from setuptools import setup, find_packages

setup(
    name="Rajscantool",
    version="2.0.0",
    author="Mr. Raj",
    author_email="raj.tech.hacker@protonmail.com",
    description="An advanced multi-purpose scanning tool for security researchers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RajownerTech/Rajscantool",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama",
        "rich",
        "urllib3",
        "setuptools",
    ],
    entry_points={
        "console_scripts": [
            "Rajscantool=rajscantool.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
