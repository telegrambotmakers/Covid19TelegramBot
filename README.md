## Covid19TelegramBot
**Telegram Bot which authenticate the source of covid19 weblink shared and also provide snippet information of covid19.**

## Youtube Link:
**Watch the video [here.](https://youtu.be/U22ZBdDrolg)**
  
## What it does
> Telegram Bot which authenticate the source of covid-19 related information shared online and also provide snippet information about covid-19.

 * /start - Will provide detail about the Bot
 * Sharing a link related to covid-19, Bot will help in authenticating the source of information shared
 * Mention of 'covid' in chat will prompt a question and give following options:
     * Symptoms : Bot will share link to WHO website with  covid-19 symptoms
     * Country Based :By entering the country name, Bot will provide  that country's present stats of covid-19 

## How it is built
> The application is python based Telegram Bot. From Telegram with the help of BotFather we created a new bot and bot logic was implemented using python. In python we used 'python-telegram-bot' library to help with interactive chat.
For this project authentication of the source of covid-19 related information is based on locally compiled source list **(trustedURL.json).

## Challenges
> For high-performing, resilient, proprietary contextual bot to work it needs AI solution, more specifically a conversational AI.For which we used RASA Framework, but it need more time and research to fully utilize the potential of the framework.To authenticate the source of online information there is no standard international database, so has to use locally compiled online source list *(trustedURL.json).
 
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

## Dependencies:
  * python-telegram-bot
  * requests
  * json
  * urllib
  * configparser
  
### Usage:
 * Make a Covid19TelegramBotbot and get the API token, and paste it inside `config.cfg`
 * ```$ python TelBot.py```
