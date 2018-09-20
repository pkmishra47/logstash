import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logash_test",
    version="0.0.1",
    author="Pradeep Mishra",
    author_email="pkmishra.pradeep@gmail.com",
    description="Tool to process multiple log files to centralized server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pkmishra47/logstash.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)