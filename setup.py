from setuptools import setup, find_packages

setup(
    name="uvu_todo_app",
    version="0.1.0",
    description="A task management application for UVU students and instructors.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"), 
    package_dir={"": "src"},
    install_requires=[
        "pytest>=7.0",
        "pydantic>=1.9",
        "click>=8.0",
        "rich>=10.0",
    ],
    entry_points={
        "console_scripts": [
            "uvu-todo=uvu_todo_app.main:main",  # entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: Utah License Plate!",
    ],
)
