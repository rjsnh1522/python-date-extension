import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-Pawan", # Replace with your own username
    version="0.0.1",
    author="Pawan",
    author_email="contactme@atlocal.com",
    description="Date module ext",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rjsnh1522/date-ext",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points={

    }
)
