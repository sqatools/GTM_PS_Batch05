
dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice
$ git clone https://github.com/akshaymishr/Pythoncode.git
Cloning into 'Pythoncode'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice
$ dir
New\ Text\ Document.txt  git\ hub.py
Pythoncode               second_program.py
first_program.py         third_program.py

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice
$ cd Pythoncode/

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ ls
README.md  first_program.py

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        first_program.py

nothing added to commit but untracked files present (use "git add" to track)

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git add .

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   first_program.py


dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git commit -m "adding my first file"
[main 1120af6] adding my first file
 1 file changed, 1 insertion(+)
 create mode 100644 first_program.py

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git commit -m "adding my first file"
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 310 bytes | 310.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/akshaymishr/Pythoncode.git
   dfce26a..1120af6  main -> main

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        second_program.py

nothing added to commit but untracked files present (use "git add" to track)

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git add .

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   second_program.py


dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git commit -m "adding second file"
[main 4310fa1] adding second file
 1 file changed, 1 insertion(+)
 create mode 100644 second_program.py

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 347 bytes | 173.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/akshaymishr/Pythoncode.git
   1120af6..4310fa1  main -> main

dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   third_program.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/


dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   third_program.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/


dell@DESKTOP-SIO6NKG MINGW64 /c/Python Practice/Pythoncode (main)
$
