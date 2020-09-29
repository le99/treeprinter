import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="treeprinter",
    version="0.0.1",
    author="le99",
    author_email="le.florez602@uniandes.edu.co",
    description="Printing a binary tree, based inspired by a solution by michal.kreuzman's solution: https://stackoverflow.com/questions/4965335/how-to-print-binary-tree-diagram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)