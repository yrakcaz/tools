#!/bin/sh

[ -z $PREFIX ] && PREFIX=/usr/local
[ -z $MAN ] && MAN=apt-get

$MAN install sudo clang vim vim-nox ctags git tmux openbox tint2 zsh tree i3lock mutt git-email

git submodule init
git submodule update

git clone https://github.com/tarjoilija/zgen.git "${HOME}/.zgen"

cp -r dotfiles/.??* ~

cp -r scripts/* $PREFIX/bin

make -C src/args/ PREFIX=$PREFIX all install clean
make -C src/demonizer/ PREFIX=$PREFIX all install distclean
