# Bash script for prepping project dependencies and starting up programs.
# Linux environment required.
# Version: Python 3.6
pwd

echo -e "Starting to install python flask dependencies...\n\n"

pip3 install -r Requirements.txt

echo -e "Opening 2nd bash terminal and running test.py..."

sh ./runTestPy.sh &

echo -e "\n\nInstallation complete, running main.py...\n\n"

python3 main.py


