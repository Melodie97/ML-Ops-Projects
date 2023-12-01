from setuptools import find_packages, setup

setup(
    name="Dagster_Demo_project",
    packages=find_packages(exclude=["Dagster_Demo_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
