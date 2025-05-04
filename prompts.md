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
Implement the #login.feature  using Flask and Jinja. Implement the #sym:serve  function using the models from #file:models.py  and #sym:ENGINE 

Add any needed templates. Use bootrstarp for the styles.

All available users are the options in the #sym:UserTypes 

Passwords are stored in plain text in the password column of the #sym:User  model
---
Add the necesary deps to pyproject.toml and install them

Start the dev webserver
---
Add a bootstrap function to #file:main.py creates demo users for all valid types. Call it inside main().
---
Which values in #file:ren.csv are not consistent with their column name?
---
Write a Pydantic validator in ren_validator.py for the rows of #file:ren.csv.

Change boolean representing values to Python booleans
Change dimensional lower-cased and upper-cased equivalent values to upper case
---
Change date values to python dates
Change date-time values to datetimes
---
Write a SQLAlchemy table with the fields from #ren_validator.py and store it in ren_model.py
---
Refactor to the style of #fetch:https://docs.sqlalchemy.org/en/20/orm/quickstart.html
---
Add enums for the columns with multiple options, use the enums as types
