#!/bin/sh
curl -sL https://codeberg.org/jbruchon/libjodycode/tags 2>/dev/null |sed -ne 's,.*code/archive/v\(.*\).tar.gz.*,\1,p' |head -n1

