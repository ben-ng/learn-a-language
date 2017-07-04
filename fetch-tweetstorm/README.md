# Fetch Tweetstorm

Given the ID of the last tweet in a reply-chain of tweets, print the tweets in chronological order. Start by printing the screen name of the author and the creation date of the first tweet. Underline the first line with `=`.

```sh
# Create a Twitter app on their developer site, then
# get CONSUMER_KEY and CONSUMER_SECRET from your Application Settings
# at https://apps.twitter.com/app/your_app_id/keys
./solution.lang CONSUMER_KEY CONSUMER_SECRET TWEET_ID
```

You can use [this tweet](https://twitter.com/sarahmei/status/880970153583718401), `880970153583718401` as your starting tweet ID.

## Typical Skills Demonstrated

1. HTTPS requests
2. JSON parsing
3. Base64 encoding
4. Recursion

## Sample Output

```md
@sarahmei, at Sat Jul 01 00:19:36 +0000 2017
============================================

We have great automatic tools to help us communicate _style_ conventions in a codebase: linters &amp; preprocessors like rubocop, jshint, etc.

These tools start to run into trouble when we use them to communicate _design_ conventions.

We don't have tools for that, and to be honest, I don't think we can write such tools.

Design conventions need to live in the heads of the folks writing code. But how do you get it there? We have lots of bad solutions for that.

The many ways we've tried &amp; failed to communicate our software design conventions:
1. wikis
2. READMEs
3. github issues
4. email threads

5. design meetings
6. code review
7. pair programming

These are approximately in ascending order of usefulness.

But even my favorite, pair programming, often falls short, especially in cultures that value remote, distributed, and/or asynchronous work.

I've been thinking lately about how to find &amp; articulate the goals/values/guiding principles of your codebase. They're often not obvious.

What I realized today is that if you _can_ articulate them, they can replace all those suboptimal solutions for design conventions.

They're like...linter rules you load into your head, and apply to the everyday software design you do when you're working in a codebase.

I know this seems terribly abstract.

The context is that I've been putting together a workshop that helps a team articulate their codebase's guiding principles.

But I've been struggling with how to explain _why_ it's valuable to have those principles. Why should anyone pay me for this?

And it occurred to me today that it's because a codebase's guiding principles efficiently communicate its _ code design_ conventions.

As opposed to a codebase's _code style_ conventions, which can be automated via rubocop, jshint, et al.

Guiding principles of a codebase are at least one level up from anything directly to do with code or its organization (patterns, etc.).

They're things like:
"make it easier for junior devs to contribute"
or
"make it faster for existing devs on the team to make changes"

Arguments about design usually stem from unarticulated differences of opinion on 1) what the principles are &amp; 2) their relative importance.

Articulating the principles doesn't mean you won't have disagreements about whether a particular design choice helps or hinders them.

But when you do have disagreements, you can skip all the "it's idiomatic" &amp; "in my 20 yrs experience I think it's better this way" bullshit.

You can go directly to discussing the only two real issues: which principle is most important here, &amp; how does this design choice help it?

As far as what the principles themselves are, it feels like there's two layers: first, a layer structured sort of like the agile manifesto.

Meaning, there are several pairs of concepts that are often in tension, and you need to figure out which side of the pair you value more.

In agile-manifesto-land, these concept pairs are things like "working code" and "comprehensive documentation."

The concepts are not mutually exclusive, but a process tends to favor one or the other. That's what I mean when I say they're in tension.

When it's a codebase, rather than a process, the concept pairs are different. But the structure is the same.

Each pair is somewhat in tension, you tend to value one over the other, &amp; each one makes sense to value in some situations but not others.

Some of the concept pairs I've been kicking around:
abstraction &lt;-&gt; findability
consistency &lt;-&gt; incremental improvement

I don't feel like I have a complete list of the concept pairs I need yet. Even those ones aren't quite using the right words.

But even from what I do have, it's clear that talking as a team about which side of each you value more is in &amp; of itself a useful exercise.

But something like "incremental improvement" is not a useful guiding principle. It's too abstract. It doesn't say what the goal is.

So from your "codebase manifesto," you then need to bubble up the principles - what are we trying to DO when we value X more than Y?

That's where you start to articulate something concrete enough to be a useful guiding principle.

Something like "make it easier for a junior dev to contribute."

Armed with two layers of guidance - the manifesto &amp; the principles - developers in my experience start making surprisingly similar choices.

Arguments are reduced, &amp; the ones you do have are less heated. And even better, more people can contribute to the design discussions.

Junior developers sometimes feel like they have nothing to contribute if two more senior folks are debating some design choice.

But when you remove the option to argue based on "experience" or "preference" and instead focus on the principles, everyone can participate.
```
