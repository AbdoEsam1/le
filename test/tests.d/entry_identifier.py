#!/bin/bash

. vars


Scenario 'Multiline collector'


Testcase 'Default setting takes data line by line'


$LE init --account-key=$ACCOUNT_KEY --host-key=$HOST_KEY --hostname myhost
#e Initialized

tee >>"$CONFIG" <<EOF
pull-server-side-config = False
[Web]
token = 89caf699-8fb7-45b1-a41f-ae111ec99148
path = $TMP/example.log
EOF
touch example.log
$LE --debug-transport-events monitor &
#e Configuration files loaded: sandbox_config
#e Following $TMP/example.log
#e Opening connection 127.0.0.1:10000 
LE_PID=$!

sleep 1
echo 'First message' >> example.log
echo 'Second message' >> example.log
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web First message
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web Second message
sleep 1
echo 'Third message' >> example.log
echo 'Fourth message' >> example.log
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web Third message
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web Fourth message
sleep 1

kill $LE_PID
wait $LE_PID 2>/dev/null || true



Scenario 'Collecting multiline entries based on specified pattern'

$LE init --account-key=$ACCOUNT_KEY --host-key=$HOST_KEY --hostname myhost
#e Initialized

tee >>"$CONFIG" <<EOF
pull-server-side-config = False
[Web]
token = 89caf699-8fb7-45b1-a41f-ae111ec99148
path = $TMP/example.log
entry_identifier = separator
EOF


Testcase 'Complex behavior pattern including time separation'


touch example.log
$LE --debug-transport-events monitor &
#e Configuration files loaded: sandbox_config
#e Following $TMP/example.log
#e Opening connection 127.0.0.1:10000 
LE_PID=$!

sleep 1
echo 'separatorLine 0' >> example.log
echo 'Line 1' >> example.log
echo 'separatorLine 2' >> example.log
echo 'Line 3' >> example.log
echo 'Line 4' >> example.log
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web separatorLine 0 Line 1
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web separatorLine 2 Line 3 Line 4
sleep 1
echo 'Line 5' >> example.log
echo 'separatorLine 6' >> example.log
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web Line 5
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web separatorLine 6
sleep 1

kill $LE_PID
wait $LE_PID 2>/dev/null || true










Scenario 'Configuration precedence'


Testcase 'Testing entry separator for section only'


$LE init --account-key=$ACCOUNT_KEY --host-key=$HOST_KEY --hostname myhost
#e Initialized

tee >>"$CONFIG" <<EOF
pull-server-side-config = False
[Web]
token = 89caf699-8fb7-45b1-a41f-ae111ec99148
path = $TMP/example.log
entry_identifier = separator
EOF


touch example.log
$LE --debug-transport-events monitor &
#e Configuration files loaded: sandbox_config
#e Following $TMP/example.log
#e Opening connection 127.0.0.1:10000 
LE_PID=$!

sleep 1
echo 'separatorLine 0' >> example.log
echo 'Line 1' >> example.log
echo 'separatorLine 2' >> example.log
echo 'Line 3' >> example.log
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web separatorLine 0 Line 1
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web separatorLine 2 Line 3
sleep 1

kill $LE_PID
wait $LE_PID 2>/dev/null || true


Testcase 'Testing entry separator defined in global context'


$LE init --account-key=$ACCOUNT_KEY --host-key=$HOST_KEY --hostname myhost
#e Initialized

tee >>"$CONFIG" <<EOF
pull-server-side-config = False
entry_identifier = separator
[Web]
token = 89caf699-8fb7-45b1-a41f-ae111ec99148
path = $TMP/example.log
EOF


touch example.log
$LE --debug-transport-events monitor &
#e Configuration files loaded: sandbox_config
#e Following $TMP/example.log
#e Opening connection 127.0.0.1:10000 
LE_PID=$!

sleep 1
echo 'separatorLine 0' >> example.log
echo 'Line 1' >> example.log
echo 'separatorLine 2' >> example.log
echo 'Line 3' >> example.log
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web separatorLine 0 Line 1
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web separatorLine 2 Line 3
sleep 1

kill $LE_PID
wait $LE_PID 2>/dev/null || true


Testcase 'Testing entry separator precedence order'


$LE init --account-key=$ACCOUNT_KEY --host-key=$HOST_KEY --hostname myhost
#e Initialized

tee >>"$CONFIG" <<EOF
pull-server-side-config = False
entry_identifier = dabra
[Web]
token = 89caf699-8fb7-45b1-a41f-ae111ec99148
path = $TMP/example.log
entry_identifier = abraka
EOF


touch example.log
$LE --debug-transport-events monitor &
#e Configuration files loaded: sandbox_config
#e Following $TMP/example.log
#e Opening connection 127.0.0.1:10000 
LE_PID=$!

sleep 1
echo 'abrakaLine 0' >> example.log
echo 'dabraLine 1' >> example.log
echo 'abrakaLine 2' >> example.log
echo 'dabraLine 3' >> example.log
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web abrakaLine 0 dabraLine 1
#e 89caf699-8fb7-45b1-a41f-ae111ec99148<14>1 ISODATETIME myhost Web - - - hostname=myhost appname=Web abrakaLine 2 dabraLine 3
sleep 1

kill $LE_PID
wait $LE_PID 2>/dev/null || true

