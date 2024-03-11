# Fundamental Git Commands :
:)
1. Initialize git in your working folder. -> **git init**

2. To create the readme markdown file -> **git add README.md** [first create this file, make changes and add it]

3. Add all the changes to the current branches staging area -> **git add .**

4. Commit (track) whenever necessary -> **git commit -m "HELLO WORLD"**

5. Check current branch/commit status etc --> **git status**

6. First push to main. -> **git push -u origin main**
	- From second pushes use this. -> **git push origin main**

7. Create new branch. -> **git branch branch_name**

8. Check in which branch. -> **git branch -a**

9. Switch to another branch. -> **git checkout anotherbranch**

10. Go to main or respective branch where the other branch will be merged and use this to merge it. -> **git merge anotherbranch**

11. Bring the main or desired branch to local repository using: -> **git pull origin main**

12. Remove file only from remote repo. -> **git rm --cached filename**
					then make commit and push
13. Remove file from both remote and local repo -> **git rm filename**
					then make commit and push