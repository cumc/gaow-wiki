# Welcome to the lab!

This page is created specifically for new comers to the lab.

# Project resources

For a quick overview of what we are up to, [here](../project_resource) is a curated list of project
repositories of the lab. They are contributed by different past and current members in various styles,
but are all meant to follow good computational research practice that makes our work easy to share
and reproduce.


# Get onboard 

You should have received emails of onboarding instructions from the HR department prior to your start day. 
Please follow those to get onboard. You will have to run by a couple of offices at Columbia Medical campus 
on your start day but all should be done by lunch time.

Once you are back to your desk please email Gao your [slack](https://slack.com) account information. 
We use slack for daily communications and quick exchange of information.

Once you are added to Slack, please send Gao via Slack direct message (DM) account information (email or username) for these services:

1. [github](https://github.com): where code, results and discussions happens for all our computational projects.
2. [dynalist](https://dynalist.io): for sharing meeting notes. You are required to keep notes for every project meeting on dynalist.
3. Your Columbia UNI if you are not communicating already with your Columbia email.

You will be added to [our home page](http://statgen.us) unless you opt out of it. If you want to embed an external link for your name 
(eg pointing to your personal website, github or LinkedIn account) please DM Gao the external link. Alternatively
you can send your bio to Gao to create a page on our website ([click here](http://statgen.us/Zhiying_Xie) for an example).

As will be explained next, most of research communications will happen on slack or github. 
If you would like to talk to Gao in person please [book a meeting here](https://gaow.youcanbook.me/). 
In general I will not reach out to you for status updates unless you book me.
Successful trainees typically book one meeting every week to discuss tasks completed from previous week's meeting and figure out what to do next week.


**A note from Gao: I apologize in advance that I might slack you after hours and over the weekend but you are not obliged to get back to me until normal hours --- I do so only in case I forget to send them out if I hold on to my messages until normal hours**.

# Orientation tasks

## Task 1: Add yourself to our slack workspace

You should receive an email notification asking you to join the `statgenworkspace.slack.com` workspace on slack. Please contact Gao if you don't have it.

Here you can communicate with others in the lab via instant messaging and work on projects together in separate project channels. Some channels of interest are:

- `stand-up`
- `papers`
- `hacks-n-tricks`
- `computing-matters`
- `complex-traits` (only if you work on the Complex trait track in our Center)
- `mendelian` (only if you work on the Mendelian disease track in our Center)

### Slack tips

1. It would be great if you could upload a photo of you (or your cat if you really resent the idea of using your photo) to your slack profile.
2. Notifications: Under `Preference -> Notifications` you can configure notifications behavior for incoming new messages. I suggest choose notification option "Direct messages, mentions and keywords". Also enable "Send email notification" under "When inactive on desktop" option.
3. Speak to a person: when you are chatting in a slack channel please pin the person you want to talk to via `@`, so s/he can get a notification and respond to you faster. Otherwise the message might go unnoticed.
4. [Slack desktop app is available](https://slack.com/downloads) and is recommended because that will keep slack running on the background, for multiple slack groups you join. There is also a phone app you can choose to install.
5. Slack uses mostly markdown language to edit text, as you will learn in the next orientation task.

## Task 2: git, github.com and markdown

We assume you are comfortable with command-line interface (on Linux or Mac). This orientation task involves obtaining the source code for this wiki, make and contribute your changes.
The source code of this wiki is on github so this will be a `git` exercise --- it means you will need to install `git`, [fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo) this repo, make changes, push back to github and [create a pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests) so we can incorporate your changes to this repository.

You should receive an email notification asking you to join the github repository for lab wiki. Please contact Gao if you don't have it.

Before you make any changes to the wiki, you should learn about using `git` if you haven't used it before. Under the `orientation` folder of this repo (that you should have been granted permission to at this point) there is a Markdown file called [`5m-git.md`](5m-git) for a 5-minutes tutorial on `git`. If you are not familiar with `git` please walk through that document to learn basic git. If you are already familiar with `git`, please take a look and help improve a more advance tutorial [`git-tips.md`](git-tips) completing some of the `FIXME` tags I made on the document, or adding to it whatever tips you've learned in the past that you find useful to mention here. **Please make sure you use the best of your knowledge editing Markdown format files, that is, format things nicely and logically**.

### Text editor

Here is a personal suggestion: I use `gvim` for many years before I switched to [VS Code](https://code.visualstudio.com/) text editor --- yes it is from Microsoft but yes it is good! I now use VS Code with Vim key binding (an Extension you can find in VS Code Extension Marketplace) so I can still use keyboard conventions that I'm familiar with.

To open a particular folder (eg a github local clone) on your computer from command terminal:

```bash
cd <path to the folder>
code ./
```

### Additional reading

- [Project communication via github issues](github-issues)
- [Additional git/github tips](git-tips)

## Task 3: organize your research

This task is about good computational biology research practice.
Regardless of your focus (on methods development or applied data analysis) it is required that all computational
procedures in your daily research should be documented, well organized and version controlled (using git) for review at any point.

You can optionally choose one of the task below for organizing your research using Notebooks or Rmarkdown files,
although Notebooks (Option 1) is highly recommended unless you have strong preference in Rstudio over JupyterLab.

### Option 1: Learn and use IPython notebook and JupyterLab

With IPython notebook + JupyterLab you should develop the practice of clearly documenting what you do in research,
and communicate your results as well as the code that generated them in a self-contained document.
In particular, in a notebook you can put down notes in Markdown cells in between code cells to explain what you do.
This may be less important to computer programmers but is very important to data scientists.

An important reason we recommend Jupyter over Rstudio is because our work typically involves both interactive data analysis and bioinformatic workflows. I recommend using [SoS suite](https://vatlab.github.io/sos-docs), a workflow system (pipeline tool) for batch data analysis and a multi-language notebook for interactive analysis, for your daily computing in research. SoS uses Jupyter as its IDE.

Here are some tasks you should walk through:

1. [Install Jupyter Lab with SoS Suite](jupyter-setup), make sure you know (eg by learning from Google) how to launch Bash, R and Python notebooks and correspondingly write codes in them.
    - If you use Debian based Linux desktop (Debian or Ubuntu) [here are some recommendations](../productivity_tips/#linux-distributions) on setting up your machine.
2. Learn from [this example](https://github.com/gaow/annotation-finemap-dsc) (and the [HTML version](https://gaow.github.io/annotation-finemap-dsc/)) the suggested format to write and report computational analysis. This is a demo of a research website `jnbinder` created. The suggested format is as follows:
    1. **Title,** and in the same notebook cell **a brief one sentence summary** of what the notebook is about.
    2. **Motivation** or **Aims**: describe the problem under investigation.
    3. **Methods overview**: a high-level description of methods used to solve the problem.
    4. **Main conclusions** (not applicable to a pure workflow notebook): take home message from your investigations.
    5. **Data input and output** (if applicable): describe data used and generated from the notebook.
    6. The rest of the notebook: multiple sections of detailed steps, with interactive codes / workflows and narratives, as well as diagnostic summary statistics, plots and tables at each step.

In your future daily research you will be expected to use SoS Notebook to analyze data, document your workflows with suggested analysis report format, and make them available as websites to share with your colleagues.
We host a private webserver and provide instructions to configure your github repository to automatically publish websites to the server as soon as you push to the repository.

### Option 2: Learn and use Rstudio and workflowr

Rstudio and workflowr is alternative to JupyterLab for interactive data analysis. Rstudio is not recommended though, if your work involves data analysis implemented as bioinformatics workflows (see Task 4 below for more details).

(Contents to be updated ...)

## Task 4: Bioinformatics workflows

If your research involves large-scale genomic analysis, you can optionally complete the following tasks on Bioinformatics Workflow System:

1. Learn from these examples the very basic usage of SoS Workflow (you can find and run the first 2 at: http://sosworkflows.com):
    - [An example to turn interactive analysis to workflow](https://github.com/vatlab/sos/blob/master/development/docker-demo/examples/HomePage_Example_2.ipynb)
    - [Another example to turn interactive analysis to workflow](https://github.com/vatlab/sos/blob/master/development/docker-demo/examples/JupyterCon18/4_Notebook_to_Workflow.ipynb)
    - [A simple SoS meta-script](sos_meta_script)
2. Please try to [reproduce this example on your computer](https://vatlab.github.io/sos-docs/doc/examples/WGS_Call.html) (source code [here](https://github.com/vatlab/sos-docs/blob/master/src/examples/WGS_Call.ipynb)). In particular, note how multiple samples are processed in parallel (`group_by` in SoS) and how intermediate results can be visualized within the workflow notebook. Also note how docker containers are used to execute the workflow to help avoid installing all software dependencies and ensuring reproducible results.

### Summary: reproducible research

In sum, we emphasize heavily on reproducible research. Performing reproducible research does not necessarily cost substantial engineering overhead, 
if you approach it properly. This is what the orientation is meant for.
Your analysis should evolve over time even during the course of a day. You can start off with 
"unpolished code and unpolished narrative" for an analysis, then polish the narratives reorganizing the analysis
structure, to help you understand what you want to achieve. You then move on to polishing the codes for each analysis task.
Finally, if some codes are deemed useful more generically, you can convert them in place as SoS workflows, and add to it
a minimal working example data-set to help testing and improving it.

### Additional reading

- How to organize computational research projects
    - [This paper](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424), [this paper](http://journals.plos.org/ploscollections/article?id=10.1371%2Fjournal.pcbi.1004385) and [this post](http://nicercode.github.io/blog/2013-04-05-projects/).

## Task 5: Explore lab wiki

You are encouraged to explore the lab wiki checking out material on other pages. In particular,

- [A list of learning material](../learning_center) on various topics in computational biology.
- [A list of "must know" shell commands](../computing_tutorial/shell-must-know.html).
- [Resource sharing guideline](../project_resource/sharing-guideline).
- [New members FAQ](faq.html).
- [This and that](../this_that), tips about life on campus, the city and places to visit & eat.