#!/bin/bash

function usage {
    cat << USAGE
$0 <version> 
    <version> - The version number to use. This should increment with every release. 

    NOTE: The code that gets packaged is relative to this script file (ie. it packages
          the src directory that is located ../src relative to the location of
          this script.
USAGE
    exit 1
}


VERSION=$1
PKG_NAME='python-cloudstack'
DIR="`dirname $0`/../"
PKG_ROOT="`cd $DIR; pwd`" # translate relative path to absolute path
EXCLUDES='.git'

if [ -z "$VERSION" ]
   then
   echo "No version specified"
   usage
fi

EXCLUDE_STRING=''

for ex in $EXCLUDES
do
    EXCLUDE_STRING="$EXCLUDE_STRING --exclude=$ex"
done

echo "Packaging the code located at $PKG_ROOT"
echo "EXCLUDING THE FOLLOWING: $EXCLUDE_STRING"

TMP_DIR=/tmp/$PKG_NAME-$VERSION

rm -rf $TMP_DIR
mkdir -p $TMP_DIR || exit 1

rsync -av $EXCLUDE_STRING $PKG_ROOT/  $TMP_DIR

cd /tmp
tar -cvzf $PKG_NAME-$VERSION.tar.gz $PKG_NAME-$VERSION/

rm -rf $TMP_DIR

echo
echo
echo "Wrote /tmp/$PKG_NAME-$VERSION.tar.gz"
echo
echo

