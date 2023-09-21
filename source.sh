#! /usr/bin/bash
# Generates all source tarballs
# Usage ./source.sh prometheus-2.47.0
fedpkg prep
pushd $1
make assets
make assets-compress
rm -rf web/ui/react-app
tar czvf ../web-ui-$1.tar.gz web/ui
rm -rf vendor
go mod vendor
tar czvf ../vendor-$1.tar.gz vendor
popd

