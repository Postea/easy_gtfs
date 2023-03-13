import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy_gtfs",
    version="1.0.0",
    author="Santiago Toso",
    author_email="santiagoa.toso@gmail.com",
    maintainer="Postea",
    description="This is a fork of the the original Bondify/gtfs_functions by Santiagpo Toso. A package specifically designed to speed up some frequent GTFS spatial analyses like mapping frequncies and speeds.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Postea/easy_gtfs",
    packages=['easy_gtfs'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'geopandas >= 0.12',
        'partridge >= 1.1',
        'utm >= 0.7',
        'folium >= 0.14',
        'plotly >= 5.13',
        'jenkspy >= 0.3',
    ],
)
