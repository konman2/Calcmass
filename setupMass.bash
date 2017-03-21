mv ~/Mass-master ~/Mass
chmod +x ~/Mass/mass/mass.py
echo "PATH=$PATH:~/Mass/mass" >> ~/.bashrc
echo "alias mass='mass.py'" >> ~/.bashrc
source ~/.bashrc

