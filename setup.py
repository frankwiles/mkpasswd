from setuptools import setup

setup(
    name="mkpasswd",
    version="0.1",
    py_modules=["mkpasswd"],
    install_requires=["Click==7.0"],
    entry_points="""
        [console_scripts]
        mkpasswd=mkpasswd:cli
    """,
)
