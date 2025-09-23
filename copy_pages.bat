@echo off
set source_dir=PWD-Tools\pages
set dest_dir=pages

for %%f in (%source_dir%\*.py) do (
    copy "%%f" "%dest_dir%\pwd_%%~nxf" /Y
)
echo Done copying pages with pwd_ prefix