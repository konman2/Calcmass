mv ~/Mass-master  ~/Mass
chmod +x ~/Mass/mass/mass3.py
echo "PATH=$PATH:~/Mass/mass" >> ~/.bashrc
echo "alias mass='mass3.py'" >> ~/.bashrc
source ~/.bashrc

