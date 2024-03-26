# reporterwebhook
dead simple discord webhook to report on system information of your server

this sends the cpu usage percentage, memory usage percentage, swap usage percentage and disk percentage of your server and time of the webhook being sent straight to a channel on your discord server

## basic setup
git clone the repo

install the required pip modules (discord_webhook, psutil)

add a webhook in your discord server on a dedicated channel

edit the src to add your webhook url (sienna kindly made a dedicated section for this)

either manually run the program with `python3` or set a cron job to run it on schedule. if you are going to use a cron job please set it for a minute before you would like the webhook to be sent to give psutil time to average the cpu usage.

## contributing
feel free to open issues and pull requests if you really feel like it, only for major issues please since this is a personal project

if you need to contact us please do so through our prefered method on discord (@elliessurviving) 
