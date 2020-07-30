import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'whoosh',
]

setuptools.setup(
    name="kollocate",
    version="0.0.1",
    author="Kyubyong Park",
    author_email="kbpark.linguist@gmail.com",
    description="Collocation Search of Korean",
    install_requires=REQUIRED_PACKAGES,
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kyubyong/kollocate",
    packages=setuptools.find_packages(),
    package_data={'kollocate': ['kollocate/indexdir/_MAIN_1.toc', 'kollocate/indexdir/MAIN_vxol2ststxvi5mkc.seg']},
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)