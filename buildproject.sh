# Bash script for prepping project dependencies and starting up programs.
# Linux environment required.
# Version: Python 3.6

echo -e "Starting to install python flask dependencies...\n\n"

sudo apt install python3-pip
pip3 install -r Requirements.txt

echo -e "Opening 2nd bash terminal and running test.py..."

sh ./runTestPy.sh &

echo -e "\n\nInstallation complete, running main.py...\n\n"

python3 main.py

