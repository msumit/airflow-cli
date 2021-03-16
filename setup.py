from setuptools import setup

INSTALL_REQUIRES = ['airflow-client >= 1.0.0', 'rich >= 0.9', 'tabulate >= 0.8']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='airflow-cli',
    version='1.0.0',
    scripts=['bin/airflow-cli'],
    author="Sumit Maheshwari",
    author_email="msumit@apache.org",
    description="Apache Airflow CLI",
    license="Apache License 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/msumit/airflow-cli",
    install_requires=INSTALL_REQUIRES,
    packages=['airflow_cli'],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)