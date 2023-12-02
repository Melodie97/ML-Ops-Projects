from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="Dagster_Demo_project",
        packages=find_packages(exclude=["Dagster_Demo_project_tests"]),
        install_requires=[
            "dagster",
            "dagster-cloud",
            "PyGithub",
            "matplotlib",
            "pandas",
            "nbconvert",
            "nbformat",
            "ipykernel",
            "jupytext",
        ],
        extras_require={"dev": ["dagster-webserver", "pytest"]},
    )
