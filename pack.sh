rm -rf pack
mkdir pack
cd pack
mkdir My_first_program
cp -r ../../My_first_program/My_first_program My_first_program/
find My_first_program/ -name __pycache__|xargs rm -rf
find My_first_program/ -name *.pyc|xargs rm -f
cp ../setup.py My_first_program
cp ../requirements.txt My_first_program
cp ../README.md My_first_program
cp ../VERSION.txt My_first_program
version=$(cat My_first_program/VERSION.txt)
tar -czf My_first_program.$version.tar.gz My_first_program


