#!/bin/bash

echo "Building..."

echo "Combining JS libraries (in specific order)"
cat js/libs/jquery-1.7.1.min.js > js/libs.combined.min.js
echo >> js/libs.combined.min.js
cat js/libs/handlebars-1.0.rc.1.min.js >> js/libs.combined.min.js
echo >> js/libs.combined.min.js
cat js/libs/tabletop-zzolo.master-20130402.min.js >> js/libs.combined.min.js
echo >> js/libs.combined.min.js
cat js/libs/jquery.isotope.v1.5.21.min.js >> js/libs.combined.min.js
echo >> js/libs.combined.min.js
cat js/libs/jquery.ba-resize.v1.1.min.js >> js/libs.combined.min.js
echo >> js/libs.combined.min.js
cat js/libs/jquery.imagesloaded.v2.1.0.min.js >> js/libs.combined.min.js
echo >> js/libs.combined.min.js

echo "Uglifying vertical timeline script"
uglifyjs js/jquery-veritcal-timeline.js > js/jquery-veritcal-timeline.min.js

echo "Now you should commit and tag a new version!"