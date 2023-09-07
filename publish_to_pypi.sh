#!/bin/bash

# chmod +x publish_to_pypi.sh
# ./publish_to_pypi.sh

# Step 1: Build the distribution packages
python setup.py sdist bdist_wheel

# Step 2: Upload the distribution packages to PyPI using twine
twine upload dist/*

# Step 3: Clean up the temporary build files (optional)
rm -rf build dist *.egg-info

git add . && git commit -m 'auto commit' && git push