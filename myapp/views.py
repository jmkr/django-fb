# Create your views here.
import facebook
import random
from django.shortcuts import render
from django_facebook.decorators import canvas_only
from django.http import HttpResponseRedirect
from django.utils import simplejson


QUOTES = [
    "Programmer - an organism that turns coffee into software. ",
    "Programming is like sex.  One mistake and you have to support it for the rest of your life.  ~Michael Sinz",
    "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.  ~Martin Golding",
    "Sometimes it pays to stay in bed in Monday, rather than spending the rest of the week debugging Monday's code.  ~Dan Salomon",
    "Beta.  Software undergoes beta testing shortly before it's released.  Beta is Latin for 'still doesn't work.'  ~Author Unknown",
    "Don't argue with people who write with digital ink and pay by the kilowatt-hour.  ~Don Rittner",
    "Any fool can write code that a computer can understand.  Good programmers write code that humans can understand.  ~Martin Fowler",
    "One man's crappy software is another man's full time job.  ~Jessica Gaston",
    "He who hasn't hacked assembly language as a youth has no heart.  He who does so as an adult has no brain.  ~John Moore",
    "If debugging is the process of removing bugs, then programming must be the process of putting them in.  ~Edsger Dijkstra",
    "Programs for sale:  fast, reliable, cheap - choose two.  ~Author Unknown",
    "It's very easy to be different, but very difficult to be better. ~Jonathan Ive",
    "Creating something out of thin air is easy. It's finding the air that's hard. ~Asher Trotter",
    "I mean there's a fun in being hated, it puts a fire in your ass and it gets fucking boring to be loved by everyone. ~James Hetfield",
    "Programmers are meant to be loved, not to be understood.",
    "To some degree, to be creative you have to be selfish. ~Meredith Norwood",
    "Simplicity is not the goal. It is the by-product of a good idea and modest expectations. ~Paul Rand",
    "There are no bad ideas, just bad decisions. ~Jacob Cass",
    "Programming today is a race between software engineers striving to build bigger and better idiot-proof programs, and the Universe trying to produce bigger and better idiots. So far, the Universe is winning. ~Rick Cook",
    "Software is like sex: it's better when it's free. ~Linus Torvalds",
    "Managing senior programmers is like herding cats. ~Dave Platt",
    "A programmer is someone who solves a problem you didn't know you had in a way you don't understand. ~Author Unknown",
    "Its amazing how the World begins to change through the eyes of a cup of coffee!! ~Donna Favors",
    "Life is not fair; get used to it. ~Bill Gates",
    "Be nice to nerds. Chances are you'll end up working for one. ~Bill Gates",
    "Your most unhappy customers are your greatest source of learning. ~Bill Gates",
    "Life is not divided into semesters. You don't get summers off and very few employers are interested in helping you find yourself. ~Bill Gates",
    "640K ought to be enough for anybody. ~Bill Gates",
    "Intellectual property has the shelf life of a banana. ~Bill Gates",
    "A cup of coffee commits one to forty years of friendship. ~Turkish Proverb",
    "Real programmers use C since it's the easiest language to spell.",
    "If you can't convince them, confuse them. ~Harry S. Truman",
    "Computers have enabled people to make more mistakes faster than almost any invention in history, with the possible exception of tequila and hand guns. ~Mitch Radcliffe",
    "A computer once beat me at chess, but it was no match for me at kick boxing. ~Emo Philips",
    "The computing field is always in need of new cliches. ~Alan Perlis",
    "I do not fear computers. I fear the lack of them. ~Isaac Asimov",
    "Computers are useless. They can only give you answers. ~Pablo Picasso",
    "The computer is a moron. ~Peter Drucker",
    "It's not the paper's fault that so much shit is printed. ~Alejandro Magallanes",
    "Everybody is a user experience designer. ~Whitney Hess",
    "I think there is a world market for maybe five computers. ~Thomas Watson",
    "There's always one more bug. ~Author Unknown",
    "Do you create anything, or just criticize others work and belittle their motivations? ~Steve Jobs",
    "Do the things that you love, the rest will come. ~Chan Yi Seng",
    "Don't find fault, find a remedy. Anybody can complain. ~Henry Ford",
    "People don't know what they want until you show them what they want. ~Steve Jobs",
    "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma - which is living with the results of other people's thinking. Don't let the noise of others' opinions drown out your own inner voice. ~Steve Jobs",
    "Brand is what people say about you after you've left the room. ~Dharmesh Shah",
    "Venture capital is neither necessary nor evil. ~Dharmesh Shah",
    "Why join the Navy if you can be a pirate? ~Steve Jobs",
    "Invest in the experience, not the product, and everyone wins. ~Dharmesh Shah",
    "Customers are very good at finding problems, not at finding solutions for those problems. ~Dharmest Shah",
    "Software that's boring will never turn into a movement. ~Seth Godin",
    "The reason to fit in is to be ignored. ~Seth Godin",
    "Competence is no longer a scarce commodity. ~Seth Godin",
    "The hard part of feature design... what to leave out. ~Dan Bricklin",
    "Fall in love with the problem, not the solution. ~Peldi Guilizzoni",
    "Create something so good people will want to copy it. ~Peldi Guilizzoni",
    "Be so good they can't ignore you. ~Peldi Guilizzoni",
    "Too many of us are not living our dreams because we are living our fears. ~Les Brown",
    "Being realistic is the most commonly traveled road to mediocrity. ~Will Smith",
    "Creativity comes from constraints. ~Biz Stone",
    "If companies don't know that they can run out of money, they won't be thinking of ways not to run out of money. ~Bill Gross",
    "Any customer can have a car painted any colour that he wants so long as it is black. ~Henry Ford",
    "There is no finish line. So love the journey. ~David Weekly",
    "You are the most powerful force in your life. ~Brian Wong",
    "Innovation distinguishes between a leader and a follower. ~Steve Jobs",
    "Nothing works better than just improving your product. ~Joel Spolsky",
    "Turn a perceived risk into an asset. ~Aaron Patzer",
    "Every feature has some maintenance cost, and having fewer features lets us focus on the ones we care about and make sure they work very well. ~David Karp",
    "It's not we need new ideas, but we need to stop having old ideas. ~Edwin Land",
    "Don't be cocky. Don't be flashy. There's always someone better than you. ~Tony Hsieh",
    "The value of an idea lies in the using of it. ~Thomas Edison",
    "Markets come and go. Good businesses don't. ~Fred Wilson",
    "Theory is splendid but until put into practice, it is valueless. ~James Cash Penney",
    "Anything that is measured and watched, improves. ~Bob Parsons",
    "The key to getting a reputation for being brilliant is actually being brilliant, not just acting like you are. ~Seth Godin",
    "Fortunes are built during the down market and collected in the up market. ~Jason Calacanis",
    "The world hates change, yet it is the only thing that has brought progress. ~Charles F. Kettering",
    "To the user, the interface is the product. ~Aza Raskin",
    "When you are small, you have to be very focused and rely on your brain, not your strength. ~Jack Ma",
    "When you're a one man show you have to focus on the most important thing to get done today. ~Noah Everett",
    "Running a startup is like being punched in the face repeatedly, but working for a large company is like being waterboarded. ~Paul Graham",
    "I try not to make any decisions that I'm not excited about. ~Jake Nickell",
    "A milestone is less date and more definition. ~Michael Lopp",
    "See things in the present, even if they are in the future. ~Larry Ellison",
    "If you're going to put your product in beta - put your business model in beta with it. ~Joe Kraus",
    "I'm always afraid of failing. It's great motivation to work harder. ~Mark Cuban",
    "Bootstrapping is a way to do something about the problems you have without letting someone else give you permission to do them. ~Tom Preston-Werner",
    "You can't make anything viral, but you can make something good. ~Peter Shankman",
    "Make every detail perfect and limit the number of details to perfect. ~Jack Dorsey",
    "It became an exercise to reduce and reduce, but it makes it easier to build an easier for people to work with. ~Jonathan Ive",
    "For every new feature we add, we take an old one out. A lot of big sites don't do that, and it's a problem. ~David Karp",
    "When something really shitty happens we try not to take it personally, figuring that tomorrow is another day. ~Mike Hudack",
    "Ideas are commodity. Execution of them is not. ~Michael Dell",
    "Success and profitability are outcomes of focusing on customers and employees, not objectives. ~Jack Ma",
    "It's simple until you make it complicated. ~Jason Fried",
    "Most people are searching for a path to success that is both easy and certain. Most paths are neither. ~Seth Godin",
    "Creativity is the sudden cessation of stupidity. ~Edwin Land",
    "Learn not to add too many features right away, and get the core idea built and tested. ~Leah Culver",
    "Do what you love and the rest will come. ~Dennis Crowley",
    "Talk to your customers. Find out what they need. Don't pay any attention to the competition. They're not relevant to you. ~Joel Spolsky",
    "I'd like to show an improved product rather than just talk about things we might do. ~Mark Zuckerberg",
    "Good is the enemy of great. ~Jim Collins",
    "No one gives a damn about the size of your to-do list. ~Ryan Freitas",
    "Do, or do not. There is no 'try'. ~Yoda",
]

@canvas_only
def home(request):
    me = request.facebook.graph.get_object('me')
    access_token = request.facebook.graph.access_token
    quote = random.choice(QUOTES)
    return render(request, 'home.html', {'me': me, 'access_token': access_token, 'quote': quote})

def reload(request):
    me = request.facebook.graph.get_object('me')
    access_token = request.facebook.graph.access_token
    quote = random.choice(QUOTES)
    return render(request, 'home.html', {'me': me, 'access_token': access_token, 'quote': quote})

def update_status(request):
    access_token = request.POST['access_token']
    submit = request.POST.get('cancel', None)

    if submit:
        #me = simplejson.loads(request.POST['me'])
        #print me
        graph = facebook.GraphAPI(access_token)
        me = graph.get_object('me')
        quote = random.choice(QUOTES)
        return render(request, 'home.html', {'me': me, 'access_token': access_token, 'quote': quote})
    else:
        quote = request.POST['quote']
        graph = facebook.GraphAPI(access_token)
        graph.put_object("me", "feed", message=quote)
        return render(request, 'all_done.html')
