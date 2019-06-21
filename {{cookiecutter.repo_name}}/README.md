# {{ cookiecutter.repo_name }}

## Setup

1. Run installation into ableton remote midi scripts directory:

```
./install_osx.sh
```

Install script creates symbolic link to this repository package
in Live 10 global remote script directory (needs sudo). If you don't want this, just copy {{ cookiecutter.package_name }} to
remote midi script directory.

2. Restart Ableton

3. Add {{ cookiecutter.package_name }} as control surface

4. (Optionally) check in log that everything runs fine
