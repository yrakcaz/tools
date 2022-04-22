# Aliases

## Git

alias st='git status'
alias add='git add'
alias all='git log --oneline --graph --decorate --all'
alias commit='git commit'
alias checkout='git checkout'
alias push='git push'
alias pull='git pull'
alias lines="git ls-files | xargs -n1 git blame --line-porcelain | sed -n 's/^author //p' | sort -f | uniq -ic | sort -nr"

## Misc

alias reload='source ~/.zshrc'
alias mg='./configure --with-debug && make'
alias poweroff='/sbin/halt'
alias reboot='/sbin/reboot'
alias rm='rm -i'
alias vo='vim -O'
alias tree='tree -C'
alias lock='i3lock'

## Arista

alias connect='mosh zac@us229'


# Misc

ulimit -c unlimited
bindkey -e emacs
bindkey \^U backward-kill-line
export EDITOR=vim
export PATH=/Library/TeX/texbin/:$PATH
export PATH=/usr/local/opt/tcl-tk/bin:$PATH
export PATH="/usr/local/opt/binutils/bin:$PATH"
export PI='pi@192.168.0.50'


# Plugins

source $HOME/.zgen/zgen.zsh

if ! zgen saved; then
    zgen oh-my-zsh
    zgen oh-my-zsh plugins/git
    zgen oh-my-zsh themes/afowler
    zgen save
fi
