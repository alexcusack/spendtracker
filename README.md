# spendtracker
Receive a text message with daily and weekly transaction summaries after every card swipe 


### Using the app directly
If you use Chase bank you can use the app directly.
1. Text 'Signup' to (616) 229-3185‬
2. On chase.com, log into your account and add the email address you were sent as one of the emails on your account
3. Then, go into Settings > Alerts > Choose Alerts > Protection and security and toggle on the first alert with the alert threshold set to $0.00
4. You're all set! You should start recieving alerts 


### How does this work
Everytime you swipe your card an alert email is sent to `<your-number>@spndtrckr.com`. The mail server http://www.cloudmailin.com/ parses this as JSON and forwards it to spndtrckr.com (http://spndtrckr.com/ping)
The spndtrckr.com service parses the email, saves the amount, date, and vendor and sends you a text like the below iwht a spending summary. 

```
$35.81 was just spent @ lyft *ride tue 6am
$68.82 so far today.
$172.88 so far this week.
```

### Development
```
./manage.py test
```

```
 ./manage.py runserver
```

### Notes 
* Right now this app only works with Chase.com, since that's the only bank I use :). If you'd like to use it with an alternate bank, it should be just a matter of adding a new/custom parser. Feel free to submit a PR. 
* This app was written when learning python for another project, so if you know better idioms feel free to push PRs fixing and refactoring whatever :)


Using email for push notifications was inspired by http://gduverger.com/secret-api-banks
