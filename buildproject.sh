# Bash script for prepping project dependencies and starting up programs.
# Linux environment required.
# Version: Python 3.6

echo "Starting to install python flask dependencies...\n\n"

pip3 install -r Requirements.txt

echo "\n\nInstallation complete, running main.py..."

python3 main.py

echo "API and flask server up and running, opening 2nd bash terminal and running test.py..."

sh ./runTestPy.sh

