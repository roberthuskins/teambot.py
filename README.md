# teambot.py
Regardless of the fact that I do not have a great name for this, this discord bot generates random Pokemon teams in a [smogon tier](https://bulbapedia.bulbagarden.net/wiki/Tier) of the user's choice. The user is given an import to use on [Pokemon Showdown](https://pokemonshowdown.com/).

#### This is an old project that runs on the pre 1.0 version of discord.py, as such it is discontinued.

## How to run:
`YOUR_TOKEN_HERE` in run.py is where you put your discord API token.  
Teambot runs off of [the discord.py api wrapper](https://github.com/Rapptz/discord.py), so you'll need to use Python 3 alongside their package.

To install discord.py,  
`pip3 install discord.py`

To run the bot,  
`python3 run.py`

When you successfully [add your discord bot to your server](https://github.com/jagrosh/MusicBot/wiki/Adding-Your-Bot-To-Your-Server), the users will see something straightforward like this.  
![](https://i.imgur.com/mcnQUB0.png)

typing `-team OU` in my discord gave me [this example](https://pokepast.es/3a4b534535ff669a) of a random team.¹

### Credits:
* API Wrapper: https://github.com/Rapptz/discord.py
* Pokemon movesets: https://github.com/Zarel/Pokemon-Showdown/blob/master/data/factory-sets.json
* All Pokemon are trademarks of The Pokémon Company.

### Notes:
1. I'm not affiliated with pokepast.es, it's just a nice way to store the raw text the bot gives you. The actual message looks [like this](https://i.imgur.com/MuDaDkk.png).
