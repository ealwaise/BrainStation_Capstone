# Project Overview
This is a capstone project for January-April 2024 BrainStation bootcamp in data science. The goal of the project is to use machine learning to analyze posts from the Stack Exchange. The Stack Exchange is a network of Q&A sites focused on various fields, such as mathematics and physics. This project focuses on the data science, software engineering, and UX (user-experience) sites.

Question askers might wonder what factors, such as time of day, subject tags, and post content determine the likelihood of a question receiving an answer. This problem will be the main focus of the project. There are several ways we can frame the problem:
* Binary classification (did the question receive at least one answer?)
* Regression (how many answers did the question receive?).
We can also study the Stack Exchange "acceptance" mechanism, whereby a question asker formally designates an answer as satisfactory, rather than answers in general. We might want to only count a question as "answered" if an answer is posted within some fixed amount of time.

We also wish to conduct a time series analysis of Stack Exchange activity, measured in daily posts. In particular, we would like to forecast future daily post numbers. This would be of interest to stakeholders in the Stack Exchange or anyone else concerned with the future of the website.

Some other questions we may want to address:
* What is the relationship between activity on the three Stack Exchange websites of interest?
* What trends over time can we observe in the number of questions about specific subjects (defined in terms of question tags)?

# Data
The Stack Exchange releases weekly [dumps](https://archive.org/details/stackexchange) of all user-generated data across the various sites. We use dumps downloaded on March 6, 2024 for this project. The data can also be queried online through the [Stack Exchange Data Explorer](https://data.stackexchange.com/). An [answer](https://meta.stackexchange.com/a/2678) on the Meta Stack Exchange (a Stack Exchange site whose topic is the Stack Exchange itself) provides a data dictionary for the dumps. The dump for each site contains a number of .xml files. We will only be concerned with the Posts.xml file, which contains rows that to posts. The columns are as follows:

* Id - A unique integer identifying the post.
* PostTypeId - An integer identifying the type of post.
    * 1 = Question
	* 2 = Answer
	* 3 = Orphaned tag wiki
	* 4 = Tag wiki excerpt
	* 5 = Tag wiki
	* 6 = Moderator nomination
	* 7 = "Wiki placeholder"
	* 8 = Privilege wiki
* AcceptedAnswerId - The PostTypeId of the post's accepted answer. Null if the post is not a question.
* ParentId - The PostTypeId of the question the post is answering. Null if the post is not an answer.
* CreationDate - The timestamp at which the post was created.
* Score - The score (determined by user ratings) of the post. Generally non-zero only for questions, answers, and moderator nominations.
* ViewCount - The number of views the post received.
* Body - The HTML content of the post.
* OwnerUserId - A unique integer identifying the user who created the post.
* LastEditorUserId - A unique integer identifying the last user who edited the post.
* LastEditDate - The timestamp at which the post was last edited.
* Title - The title of the post. Null unless the post is a question.
* Tags - A list of subject tags applied to the post, enclosed in <>. Null unless the post is a question.
* AnswerCount - The number of answers the post received. Null if the post is not a question.
* CommentCoutn - The number of comments on the post.
* FavoriteCoutn - The number of times the post was favorited by users.
* ClosedDate - The timestamp at which the post was closed. Null if the post was not closed.
* CommunityOwnedDate - The timestamp at which the post was community wiki'd. Null if the post was not community wiki'd.
* ContentLicense - The content license under which the post was published.