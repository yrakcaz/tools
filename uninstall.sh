#!/bin/sh

[ -z $PREFIX ] && PREFIX=/usr/local

cd dotfiles
for i in .??*
do
    rm -rf ~/$i
done

cd ../scripts
for i in *
do
    rm -rf $PREFIX/bin/$i
done

cd ..
make -C src/args/ PREFIX=$PREFIX uninstall
make -C src/demonizer/ PREFIX=$PREFIX uninstall
