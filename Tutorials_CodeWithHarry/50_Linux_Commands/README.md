# 50 Linux Commands by CodeWithHarry

*YouTube link: https://youtu.be/l32UR9DcjLg*

*CodeWithHarry link: https://www.codewithharry.com/blogpost/50-linux-commands*

**Date: 11/06/2025**

- `ls`: list the files and directories

- `cd Tutorials_CodeWithHarry/`: change directory

- `mkdir folder_test`: make a directory

- `rmdir folder_test`: remove a directory

- `pwd`: print the current working directory

- `cd ../`: Back to previous directory

- Make a file: `vim main.py`, press `i` to insert the code, `esc` to the last line, `:wq` to save and quit

- Edit a file: `vim main.py`, Do the edits, `esc`, `:wq` to save and quit or `:q!` for discard and quit

- Copy a file: `cp main.py main-backup.py`

- Move or rename: `mv main-backup.py backup.py`, `mv backup.py folder1/backup.py`

- Remove a file: `rm main.py`, Remove a folder: `rm -r folder1/`

- Create a file: `touch text1.txt`

- `cat text1.txt`: Concatante and  Display files

- `man ls`: Manual for a command

- `htop`

- `chmod`: Go to *https://chmod-calculator.com/*, `mkdir folder1`, 
`ls -lart` to see the permissions, `rwx`: read-write-execute, `chmod 740 folder1`, `ls -lart`. 

- `chown`: Change the owner of a file or directory.

- `tar`: Create or extract compressed files.

- Compress file: `gzip text1.txt`. Decompress file: `gunzip text1.txt.gz`

- `ssh`: connect to a remote server securely

- `scp`: Securely copy files between servers

- `ping github.com`: checks network connectivity. CTRL+C to exit.

- `ifconfig`: Display or configure network interfaces

- `netstats`: Display network connection info

- `route`: View or configure network routing tables

- `top` (`htop` is better)

- `ps`, `ps -ef`, `ps -ef | grep sbin`

- Terminate a process: `kill [Process ID]

- `systemctl`: Control system services and settings

- `service`: Control system services

- Add a user: `useradd skpcwh`, `passwd skpcwh`, Give a password.

- Delete a user: `userdel skpcwh`

- Switch user: `su skpcwh`, `bash`, `pwd`, `exit`, `pwd`, `bash`, `su root`, Give password, `bash`.

- `sudo`: Execure a command as another user

- `uptime`: display system uptime and load average

- `df`: display disk space usage

- `du`: display disk usage by file or directory

- Mount a file system: `sudo mount /dev/sdb1 /mnt/usb`

- Unmount a file system: `sudo umount /mnt/usb`

- `date`: display or set the system date and time

- `whoami` display the current user name

- Locate a program or command in the system path: `which python`

- Displays all the information about a user: `finger skpcwh`

- Display system information: `uname`, `uname -a`

- `history`: display a list of previously executed commands

- Display texts: `echo 'See the video of this tutorial on YouTube'`

- Redirect output to both a file and the console: `ls | tee text1.txt`

- `locate folder1`: Locates files and folders.

- `sort text2.txt`: Sort lines

- `uniq text3.txt`: Remove duplicate lines from a file or input

- display the first/last few lines of a file or input: `head README.md`, `tail README.md`. `tail -15f README.md`, CTRL+C to exit.



