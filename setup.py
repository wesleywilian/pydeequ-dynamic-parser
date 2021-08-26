from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='PydeequDynamicParser',
    packages=['PydeequDynamicParser'],
    version='0.3',
    license='apache-2.0',
    description='Python library which makes it possible to use validation rules in pydeequ based on json structures.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='wesleywilian',
    url='https://github.com/wesleywilian/pydeequ-dynamic-parser',
    download_url='https://github.com/wesleywilian/pydeequ-dynamic-parser/archive/v0.3.tar.gz',
    keywords=['pydeequ', 'json', 'data', 'quality', 'rules'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
