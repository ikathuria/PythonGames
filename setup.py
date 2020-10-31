import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PythonGames-ikathuria", # Replace with your own username
    version="0.0.1",
    author="Ishani Kathuria",
    author_email="ishani@kathuria.net",
    description="A package with lots of python games.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ikathuria/PythonGamest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)