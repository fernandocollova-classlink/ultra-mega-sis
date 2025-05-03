Write a pyproject.toml using uv for the ultra_mega_sis module in the current workspace, add the latest Sqlalchemy as a dependency. Migrate dev deps and configs from #fetch https://bitbucket.org/fernandocollova/config_files/raw/0d7213672c5944a933ecd283125b5dbd499af86f/pyproject.toml to ruff and add them to the pyproject.toml file. Pin all dependencies. Install all dependencies in a virtual env. Change the max line length to 100.
---
Write a pyproject.toml using only uv for the ultra_mega_sis module in the current workspace
---
Refactor pyproject.toml to use Hatchling as the build backend, follow the instructions in #fetch:https://hatch.pypa.io/1.13/how-to/environment/select-installer/#enabling-uv to configure it
---
Migrate dev deps and configs from #fetch https://bitbucket.org/fernandocollova/config_files/raw/0d7213672c5944a933ecd283125b5dbd499af86f/pyproject.toml to ruff and add them to the pyproject.toml file. Only use ruff.
---
Write a pyproject.toml using only PyPA tools for the ultra_mega_sis module in the current workspace, add latest sqlalchemy as dep. Pin all deps. Add configs and dev deps from #fetch https://bitbucket.org/fernandocollova/config_files/raw/0d7213672c5944a933ecd283125b5dbd499af86f/pyproject.toml. Install all deps in a venv located in .venv. Change the max line length to 100. Install all vscode extensions for the dev packages. Only install extensions from verified publishers. Classify the package as private.
---
Implement the #file:login.feature using Flask and Jinja

Add a serve() function to a new serve.py follow the signature used in the call to serve() from #file:cli.py and use the models from #file:models.py.

Add any needed templates. Use bootrstarp for the styles.

All available users are the options in the UserTypes Enum from #File: ultra_mega_sis/models.py.

Passwords are stored in plain text in the password column of the User model 
---
Add the necesary deps to pyproject.toml and install them

Start the dev webserver
---
Add a bootstrap function to #file:main.py creates demo users for all valid types. Call it inside main().
---
Write a model for the table defining the exported fields in #fetch:https://star-help.renaissance.com/hc/en-us/articles/11285507167387-Exporting-Star-CBM-Assessment-Scores-Downloading-Data-CSV-Files in a new file called ren.py
---
Add enums for the columns with multiple options, use the enums as types
