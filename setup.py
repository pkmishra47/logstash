import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="logstash",
    version="0.0.1",
    author="Example Author",
    author_email="pkmishra.pradeep@gmail.com",
    description="Package for processing log files to centralized log server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pkmishra47/logstash",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)