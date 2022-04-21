# Instructions/Documentation

## Hosting

##### Things you may need
* **[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)**
* **[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)**

##### Useful links, if you need them
* **[Beebom.com - How to Make a Discord Bot](https://beebom.com/how-make-discord-bot/)**
* **[How to Create a Discord Bot - Discord.py](https://discordpy.readthedocs.io/en/stable/discord.html)**
* **[Tech With Tim - Host a Discord Bot for Free](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwid1uCDk6X3AhUNT8AKHXGADF4QtwJ6BAgIEAE&url=https%3A%2F%2Fwww.techwithtim.net%2Ftutorials%2Fdiscord-py%2Fhosting-a-discord-bot-for-free%2F&usg=AOvVaw2y8xW1jXdjr_8ZsMa__cNv)**
* **[How to Host a Discord Bot on Heroku](https://github.com/audieni/discord-py-heroku)**

### Step 1 - Setting up a bot on the [discord developer portal](https://discord.com/developers/applications).
To host this bot, you need to go to the **[discord developer portal](https://discord.com/developers/applications)**.

1. Log in to the **discord developer portal** with your discord account.
2. If you're not already on **applications**, go to it. Click `New Application`.
3. When asked for a name, type in 'Earth Mother' and click `Create`.
4. You'll then be taken to a page where you can see your new application. Click `Bot` at the left of the screen.
5. On the right, you should see an `Add bot` button. Click it and press `Yes, do it!` when prompted to continue.
6. Now you should see your new bot. Add a profile image. It should already be called 'Earth Mother' but if not, change it here.
7. On the left of the screen, click `OAuth2`. You'll then see two options appear underneath it. Click `URL Generator`.
8. Under `Scopes`, select `bot`. Then, under `Bot Permissions`, select `Administrator`.
9. Under `Generated URL`, you should see a link. Click it to **invite** the bot to your server.
10. Go to the left of the screen and click `Bot` again. Under its username, you should see a `Reset Token` button. Click it.
11. Click `Copy`, and **keep it somewhere safe** as you'll need it later. This is sort of like your bot's password, so keep it private.

### Step 2 - Add your token

1. You should have your token from **steps 10 and 11**.
2. Go to the bot's main directory. For reference, this should have a file called `__main__.py`, and `cogs`, `files`, & `images` folders.
3. Create a file called `.env`, and open it in notepad.
4. Add the following to the file, replacing `YOUR_TOKEN_HERE` with the token from **steps 10 and 11**.

```
TOKEN=YOUR_TOKEN_HERE
```

5. Save the file and exit.

### Step 3 - Hosting the bot
There are many different options for hosting. I recommend **[Heroku](https://heroku.com/)**, as it's free and easy to use. You choose to pay for premium features if needed.

1. Create an account on **[Heroku](https://heroku.com/)**.
2. Create a **new application** and name it 'earth-mother'.

![...](https://www.techwithtim.net/wp-content/uploads/2019/02/heroku-app.png)<br>

3. Go to Settings > Add Buildpack > Python.

![...](https://www.techwithtim.net/wp-content/uploads/2019/02/heroku-build.png)
![...](https://www.techwithtim.net/wp-content/uploads/2019/02/python-build.png)<br>

4. Install the **[Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line)**. You'll need this later.
5. Go to your bots directory and run **command prompt**. Make sure you open cmd in in the **correct directory**.
6. Run the command `echo>Procfile`.

![...](https://www.techwithtim.net/wp-content/uploads/2019/02/echo.png)<br>

7. Open the file in Notepad and replace the contents (if any are there) with `worker: python __main__.py`. Then **save** it.

![...](http://techwithtim.net/wp-content/uploads/2019/02/proc.png)<br>

8. Next, we'll need to run some commands. Open **cmd** in the bot's main directory again. Run the following commands in order.

```batch
heroku login
heroku git:clone -a earth-mother
git add .
git commit -am “this is just a message. you can write whatever you want in here.”
git push heroku master
```
![...](https://www.techwithtim.net/wp-content/uploads/2019/02/output.png)

9. Lastly turn the bot on from heroku.com. Go to the **Resources** Tab and hit `Edit`. The simply click the slider so it turns on and hit `Confirm`.

![...](https://www.techwithtim.net/wp-content/uploads/2019/02/on.png)

## Changing or adding facts

1. Go to the folder where your bot is on your computer, and open the `files` folder.
2. Open `facts.xlsx`, and add facts to the sheet. DO NOT change the first row, or change the name of the file. Only add/remove facts.
3. Open **cmd** in the main folder for the bot and run the following commands:

```batch
heroku login
git add .
git commit -am “added facts. you can write whatever you want in here.”
git push heroku master
```
