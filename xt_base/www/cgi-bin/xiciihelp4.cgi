#! /bin/sh

export HLPSRV_CGIPATH="/cgi-bin/xiciihelp4.cgi?h="
export HLPSRV_IMPATH="/help-images4/"
export HLPSRV_PATH="/home/webadmin/wrcad.com/html/restricted/helplib4/xic/help"

IFS='='
set $QUERY_STRING
/usr/local/bin/hlpsrv -DXic -DXicII $2

