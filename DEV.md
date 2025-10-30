# Development

## Generate SDK

Depending on the changes, it might be necessary to delete the SDK and generate it from scratch.

```
rm -fR sdk/
```

To generate the SDK use the following command. Don't forget to update the `packageVersion`.

```
openapi-generator generate -i api.yml -g python -o ./sdk --additional-properties=packageName=attachmentav,packageVersion=0.2.0,projectName=attachmentav-virus-scan-sdk
```

The `pyproject.toml` needs to be modified manually, as the generator does not provide the necessary properties.


```
[project]
name = "attachmentav_virus_malware_scan_sdk"
version = "0.1.0"
description = "A virus scan SDK for Python. Scan files for viruses, trojans, and other kinds of malware with attachmentAV."
authors = [
  {name = "Andreas Wittig",email = "andreas@attachmentav.com"},
]
license = "MIT"
readme = "README.md"
keywords = ["virus", "malware", "scan", "scanner", "sdk"]
requires-python = ">=3.9"
```

As well as.

```
[project.urls]
Repository = "https://github.com/widdix/attachmentav-sdk-python"
```

Also, modify `setup.py` manually.

```
setup(
    name=NAME,
    version=VERSION,
    description="A virus scan SDK for Python. Scan files for viruses, trojans, and other kinds of malware with attachmentAV.",
    author="Andreas Wittig",
    author_email="andreas@attachmentav.com",
    url="https://github.com/widdix/attachmentav-sdk-python",
    keywords=["virus", "malware", "scan", "scanner", "sdk"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    An SDK to integrate virus and malware scan capabilities into Python applications. Scan files for viruses, trojans, and other kinds of malware with attachmentAV powered by Sophos.
    """,  # noqa: E501
    package_data={"attachmentav": ["py.typed"]},
)
```


## Publish

```
cd sdk
cp ../README.md .
python3 -m pip install --upgrade pip build twine
python3 -m build
# Use for testing
# python3 -m twine upload --repository testpypi dist/*
# Deploy to prod
python3 -m twine upload --repository pypi dist/*
