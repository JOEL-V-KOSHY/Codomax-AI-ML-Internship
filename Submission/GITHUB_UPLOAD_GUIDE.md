# Upload this folder to GitHub (VS Code)

1. Sign in to https://github.com/.
2. Create a new repository named `Codomax-AI-ML-Internship`.
3. Choose Public if the internship instructions require a public repository. Do not add confidential information.
4. In VS Code, open the extracted `Codomax_Module_01_Complete` folder.
5. Open Terminal → New Terminal.
6. Run these commands one at a time, replacing the URL with your own repository URL:

```bash
git init
git add .
git commit -m "Add Module 01 AI and Python learning materials"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Codomax-AI-ML-Internship.git
git push -u origin main
```

If Git asks you to identify yourself, configure your Git name and email using the values associated with your GitHub account. Never share your password or access token in chat or commit it to the repository.

After pushing, refresh the GitHub repository page and verify that the folders and files are visible.
