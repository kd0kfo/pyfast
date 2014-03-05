#!/bin/sh

echo Generating API
EPYDOC_PATH=$(which epydoc)
python $EPYDOC_PATH -v -o pyfast_api --name pyfast ../pyfast

exit

RST2MAN=rst2man.py
which $RST2MAN  &> /dev/null

if [[ $? -ne 0 ]];then
    echo Could not find $RST2MAN. Skipping...
else
    if [[ ! -d man/man1 ]];then
	mkdir man/man1
    fi
    
    $RST2MAN trident.rst > man/man1/trident.1
fi
