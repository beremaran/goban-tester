#!/usr/bin/env sh

cd /tmp;

echo "Downloading gnugo source .. (version 3.8)";
wget http://ftp.gnu.org/gnu/gnugo/gnugo-3.8.tar.gz;
echo "Extracting gnugo source ..";
tar -xf gnugo-3.8.tar.gz;
cd gnugo-3.8;

echo "Compiling and installing ..";
sudo ./configure;
sudo make;
sudo make install;

echo "Done.";
