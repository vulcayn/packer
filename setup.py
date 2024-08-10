from setuptools import setup, find_packages

setup(
    name="packer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "packer=packer.packer:main",
        ],
    },
    author="Killian von Vulcayn",
    author_email="killian@vulcayn.com",
    description="A tool to pack repository contents into a markdown file",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vulcayn/packer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="Apache License 2.0",
)