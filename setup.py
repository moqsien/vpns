from pathlib import Path
from setuptools import find_packages, setup

install_requires = [
    "certifi>=2023.5.7",
    "chardet>=5.1.0",
    "charset-normalizer>=3.1.0",
    "idna>=3.4",
    "lxml>=4.9.2",
    "Naked>=0.1.32",
    "pycryptodome>=3.17",
    "PyYAML>=6.0",
    "requests>=2.30.0",
    "shellescape>=3.8.1",
    "urllib3>=2.0.2"
]

version = (Path(__file__).parent / "free/VERSION").read_text("ascii").strip()

setup(
    name="Free",
    version=version,
    url="https://github.com/moqsien/vpns",
    project_urls={
        "Documentation": "https://github.com/moqsien/neobox",
    },
    description="A free vpns collector for neobox.",
    author="Mo Qsien",
    author_email="moqsien@foxmail.com",
    maintainer="Mo Qsien",
    maintainer_email="moqsien@foxmail.com",
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["fvpn = free.run:Run"]},
    classifiers=[
        "Framework :: Sracpy",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11",
    install_requires=install_requires,
)
