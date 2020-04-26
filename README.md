# Covid19TelegramBot
## Telegram Bot which authenticate the source of covid19 weblink shared and also provide snippet information of covid19.

# Watch the video [here.](https://youtu.be/5nhdxpoicW4)

## Dependencies:
  * python-telegram-bot
  * requests
  * json
  * urllib
  * configparser
  
## Example:
> You: /start

> AZCovid19: Hi, I am AZ Covid19 Bot

> You: Covid

> AZCovid19: Do You need any information about COVID19?

> You: Yes

> AZCovid19: Thank You! We will help you:

> AZCovid19: Please enter the country Name

> You: Germany

> AZCovid19: Country : Germany 
             Totalconfirmed : 157114 
             Totaldeaths : 5884 
             Totalrecovered : 109800

> You: Italy

> AZCovid19: Country : Italy 
             Totalconfirmed : 197675 
             Totaldeaths : 26644 
             Totalrecovered : 64928

> You: https://amp.cnn.com/cnn/2020/04/25/us/who-immunity-antibodies-covid-19/index.html#aoh=15879204458735&amp_ct=1587920543391&referrer=https%3A%2F%2Fwww.google.com&amp_tf=From%20%251%24s

> AZCovid19 : This news is not from a trusted source

### Usage:
 * Make a Covid19TelegramBotbot and get the API token, and paste it inside `config.cfg`
 * ```$ python TelBot.py```
