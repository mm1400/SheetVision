from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sheetvision",
    version="0.1.0",
    description="A tool for reading sheet music. Adapted from the original SheetVision project to run faster and output only midi.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mm1400/SheetVision",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "contourpy>=1.3.1",
        "cycler>=0.12.1",
        "fonttools>=4.56.0",
        "kiwisolver>=1.4.8",
        "matplotlib>=3.10.1",
        "MIDIUtil>=1.2.1",
        "numpy>=2.2.3",
        "opencv-python>=4.11.0.86",
        "packaging>=24.2",
        "pillow>=11.1.0",
        "pyparsing>=3.2.1",
        "python-dateutil>=2.9.0.post0",
        "six>=1.17.0",
    ],
)