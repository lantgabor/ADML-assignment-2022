#!/bin/bash
urls="http://www2.projects.science.uu.nl/shakefive/data/ShakeFive2.background.tar.bz2"
 
## let us grab it ##
for u in $urls
do
   wget "$u" -P "../data/" 
done