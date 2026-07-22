# Template

Copy `template/vulnerability/` into any category folder under `vulnerabilities/`.

Windows PowerShell:

```powershell
Copy-Item -Recurse template\vulnerability vulnerabilities\rag\example-vulnerability-name
```

Linux Bash:

```bash
cp -r template/vulnerability vulnerabilities/rag/example-vulnerability-name
```

Then fill in the files from top to bottom:

1. `README.md`
2. `lab-setup.md`
3. `assets/`
4. `secure/`
5. `demo/`
6. `blog/`
7. `evidence/`
