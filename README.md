Isaac Lance
isaacglance@gmail.com
# proj10-final
Setup meetings with log ins for meeting organizers (per-meeting login) and for invitees (per-invitee login)

## What is here
Index page:
	Select what you want to do, create a new meeting, change meeting calues and invite users, or login as a user yourself.
Meeting page:
   (New meeting)
	This is basically a sign-up page. "bcrypt" hashes and salts passwords. The way bcrypt adds salt is confusing unless you read	 	 their docs, it looks like it's missing the salt storage step if you just look at the code.)
Meeting page:
	Sign in and logout functionality is available.
	Users can be added, which sends them an email and adds them to the mongo db.
	Of course the time selection comes back looking very similar to before.
	Finally there is a button take what users have submitted so far, and process that- however I have not finished this step.

More thoughts:
Events are the only thing with passwords. An event can be edited with its password, no google account login required.
Passwords are salted and hashed by bcrypt.

Invitees are sent emails from my own email address, providing them an event id.
Invitees login with the id of the meeting, I wanted to make it so that google handled their login for me, but it
was pretty tough. So for now, you can technically add events from any calendar, nothing can stop you.
On that note, there are a lot of places where the site can be broken by a user poking around. 
If I had more time I could fix these easily, it is just time consuming.

pendulum objects cannot be held in MongDB,
Instead we output them into the db as RFC3339 strings, the same used by google.
When we retrive them from the db they can be parsed back into pendulum objects.

Default day range is 9am to 5pm. After this value is changed and accepted the values will return to their default.

##Warnings
Does not run in IE9 or earlier due to some new HTML5 stuff.

Should be fixed:
-Cannot properly handle duplicate names of any sort. It won't break but their will be weird behavior.
-Does not require a certain email address to submit a calendar, it's free game.
-Some things run slower than they could. Loops could be removed or made more efficient.
-Obviously, it's not complete. I still need to bring in the time calculation from project 8 but its already an hour past the final late due date.
-Logging out should "clear" a users google login, but figuring out how to do this was difficult for me.
