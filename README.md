# Project Overview
---
This is a capstone project for January-April 2024 BrainStation boot camp in data science. The goal of the project is to use machine learning to analyze posts from the Stack Exchange. The Stack Exchange is a network of Q&A sites focused on various fields, such as mathematics and physics. This project focuses on the data science, software engineering, and user experience sites.

Question askers might wonder what factors, such as time of day, subject tags, and post content determine the likelihood of a question receiving an answer. This problem is the main focus of the project. More precisely, we use machine learning models to predict whether or not a question will be answered within a week of posting. We approached the problem using both logistic regression and random forests.

We also conduct a time series analysis of Stack Exchange activity, measured in daily posts. In particular, for each of the three sites under study, we build models to predict the 30-day average of post numbers on a given day. This is of interest to stakeholders in the Stack Exchange or anyone else concerned with the future of the website.

# Data
---
The Stack Exchange releases weekly [dumps](https://archive.org/details/stackexchange) of all user-generated data across the various sites. We use dumps downloaded on March 6, 2024 for this project. The data can also be queried online through the [Stack Exchange Data Explorer](https://data.stackexchange.com/). An [answer](https://meta.stackexchange.com/a/2678) on the Meta Stack Exchange (a Stack Exchange site whose topic is the Stack Exchange itself) provides a data dictionary for the dumps. The dump for each site contains a number of .xml files. We will only be concerned with the Posts.xml and Comments.xml files, which provide information about user-generated posts and comments, respectively. The columns of Posts.xml are as follows:

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
* CommentCount - The number of comments on the post.
* FavoriteCount - The number of times the post was favorited by users.
* ClosedDate - The timestamp at which the post was closed. Null if the post was not closed.
* CommunityOwnedDate - The timestamp at which the post was community wiki'd. Null if the post was not community wiki'd.
* ContentLicense - The content license under which the post was published.

The columns of Comments.xml are as follows:

* Id - A unique integer identifying the comment.
* PostId - The Id of the post the comment was left on.
* Score - The score (determined by user ratings) of the post the comment was left on.
* Text - The content of the comment.
* CreationDate - The timestamp at which the post was created.
* OwnerUserId - A unique integer identifying the user who made the comment.
* ContentLicense - The content license under which the comment was published.
* UserDisplayName - The username of the user who made the comment.

# Directory Structure
---

The following folders can be found within the main project directory:

* Data - Contains all the data files used for the project.
* Images - Contains graphs and charts used to visualize data for presentation purposes.
* Notebooks - Contains the Python notebooks used to explore the data and build models.
* Presentations - Contains PDFs of slides used to present information from the project.
* Reports - Contains reports summarizing the results of the project.
* src - Contains supplementary code used within the notebooks.

More specific information about the contents of each folder can be found within the files "doc.md" located within each folder.

# Dependencies
---
This project was conducted in a Python 3.11.5 environment with the following packages installed:

* beautifulsoup4 4.12.2
* matplotlib 3.8.0
* nltk 3.8.1
* numpy 1.26.4
* pandas 2.1.4
* scikit-learn 1.2.2
* seaborn 0.12.2