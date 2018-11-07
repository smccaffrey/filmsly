import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filmsly",
    version="0.0.1",
    author="Sam McCaffrey",
    author_email="smccaffrey70@gmail.com",
    description="An API for gather real-time theatre, movie, and showime information.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smccaffrey/filmsly",
    packages=setuptools.find_packages(), #include = ['filmsly.*']['filmsly','filmsly.library','filmsly.theatres'],#
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)