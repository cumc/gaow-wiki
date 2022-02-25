# FAQ

## What programming languages do we use and what language is preferred?

Short answer: R (45%), Python (45%), and others (10%) mainly including C++ (typically with R through `Rcpp`),
BASH and SQLite. On top of these, we use [DSC](https://stephenslab.github.io/dsc-wiki) to perform simulation studies and
[SoS](https://vatlab.github.io/sos-docs/) to write analysis pipelines.

Long answer: the choice of language typically depends on the nature of the project and what has already been done for the project.
More often than not, a project involving both numerical simulation studies and real-world data analysis might require using
a combination of programming languages for different tasks. That is where DSC and SoS can be very useful in "gluing" pieces
of code in different languages together.

If an old project already has a code base using some languages and your new project is an extension of the old one, then at least at the beginning stage it is often more
beneficial to reuse existing codes thus sticking to whichever language the old project is written in. By a similar token, R language might be
more suitable to program statistical methods that involves using R packages written by others to accomplish some functionality in your method. Python
might be great to program machine learning tasks because of the well-established scikit-learn and tensorflow libraries for machine learning.

In my view no one language is preferred over another, although the researcher might be more comfortable writting in one language over another.
Generally speaking, R is great language for prototyping statistical model implementation, making simple plots, and analyzing small scale data-set.
Python is great for machine learning, data wrangling & munging, bioinformatics (many bioinformatics libraries written in Python), making complicated plots (with matplotlib),
and high performance computing (e.g., leveraging GPU and HDFS system). C++ nowadays is most suitable for optimizing pieces of codes already prototyped
in R or Python, and it is the easiest to write them as R extensions using Rcpp package -- since we often implement new statistical methods in R, it is great
to speed it up with C++ extensions. [A handful BASH commands such as `sed`, `awk`](../computing_tutorial/shell-must-know.html) are the most useful
for quick data wrangling tasks and can be a lot easier to write than R or Python codes when used to solve the problem they fit in.

This is why we promote the idea of breaking up your project to smaller problems, writing "modules" for each problem, and glue them together using tools such as
DSC and SoS pipelines. In my view, putting together casually written scripts of different languages into rigorous pipelines works much better than writing a sophisticated software program
in one language.

I want to add a caution for R language: R has some annoy pitfalls that when you commit them, they don't trigger an error message but rather falls back to some default behavior which might lead
to what seems very strange errors down the road. Hidden errors are always frustrating. For a quick example, in R the behavior below can be confusing (you can try `print(a$k)` to figure out why),

```r
> a = list(); if (a$k) print(9)
Error in if (a$k) print(9) : argument is of length zero
```

versus for Python the error behavior and message is much better,

```python
>>> a = dict()
>>> if (a['k']): print(9)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'k'
>>>
```

I also want to point out that in bioinformatics it almost always work better to use specialized tool to process specific type of data than to write your own scripts.
For example, `vcftools` (BASH) or `cyvcf2` (Python) should be used to work with `VCF` genotype file format, rather than to parse them line by line. `bedtools` should be used
to query genomic regions rather than using generic data base tools such as SQLite for the job. Specialized tools are less prone to coding errors, and typically
will work faster than your own code.

To summarize, I believe in the statement that "a good programmer writes good codes, but a great programmer reuses good codes". When you start a project
please try to think ahead into various stages of the project, and look for existing resources that you might be able to reuse for each stage. Then you take these
factors into consideration before choosing a languages. But don't get too fixated in that decision making because of two reasons. First, you can always prototype with whatever language
you like, then convert them to other languages if necessary (for performance reason, for compatibility with other packages etc.). In my opinion it is a lot easier to translate between
languages than to write new code. Secondly, with DSC and SoS you can
always switch between languages for different tasks, as long as you "modularize" your project well enough! DSC and SoS are tools developed in house thus might lack extensive
documentation and support from the community compared to other languages. But you can ask for help from others in the group who have more experiences with these tools.

## How about IDE choice: text editor, JupyterLab or Rstudio?

I personally use `vscode` with vim key binding. Before finally settle with `vscode`, I have used vim, emacs, atom and subline. I use Jupyter for interactive analysis and bioinformatics pipeline development.

Rstudio: if you use R for 90% of your research then Rstudio is perhaps way to go.

Jupyter: if you work with many languages then JupyterLab is perhaps better because with multiple kernels you can develop codes for different languages in similar environment.
With SoS kernel in JupyterLab, you can even switch between languages and transfer data among them, in the same notebook. More importantly, we promote the use of pipelines in
data analysis. Starting writing interactive codes in Juptyer and later modify them in place into pipelines written in SoS language is very straightforward. In fact such in-place
modification is one of the major design feature of SoS. In this context it makes much more sense to use JupyterLab as your IDE.

Rstudio + Jupyter: you can write interactive analysis codes for data exploration in R, and write SoS pipelines in Jupyter notebooks. If you develop R codes interactively and later want to make them pipelines, 
then you'll have to copy codes from Rmarkdown and paste them to another Jupyter file. This is extra work and is error prone --- just be warned!

Although I recommend SoS Notebook and SoS Workflow be the primary tool for daily computational research, I acknowledge there are limitations to using IPython notebooks in general for interactive analysis, [cf, this presentation](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/mobilepresent?slide=id.g362da58057_0_1). However most of such issues can be avoided if you recognize them and develop good habits in using notebooks and not commit those pitfalls. Additionally, these limitations do not apply to when you use notebooks to develop SoS Workflows; and I always prefer writing small workflows over interactive notebooks --- as you hopefully have learned from the above tasks and agree that it is almost trivial to turn an interactive SoS notebook into an SoS workflow.

