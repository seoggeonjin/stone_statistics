import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stone_statistics",  # Replace with your own username
    version="0.0.1",
    author="Stone",
    author_email="seoggeonjin@gmail.com",
    install_requires=[
        'dependency1>=1.0',
        'dependency2==2.5.0',
        'dependency3<3.0',
    ],
    description="Stone's Statistics Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)