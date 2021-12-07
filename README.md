# The Nordic Pile replication code

The Nordic Pile is a repository with the aim of providing tools and code to download and
replicate a large nordic language dataset. The dataset consists of many smaller datasets combined together.
With the objective to cover a broad set of language modalities.

## Workflow

To propose a new dataset be added to the Nordic Pile, [open an issue](https://github.com/AI-Nordics/the-nordic-pile/issues/new).
Your issue should include a description of the dataset, its size, what language(s) it is in, 
a link to the data, and any other relevant information. If a project manger approves your proposal, 
they will change its label to [![Datasets](https://img.shields.io/github/labels/EleutherAI/The-Pile/Dataset)](https://github.com/AI-Nordics/the-nordic-pile/labels/Dataset) and add it to [![Project: Datasets](https://img.shields.io/badge/Project-Datasets-lightgrey)](https://github.com/AI-Nordics/the-nordic-pile/projects/1). Datasets that we elect to not include in the current version of the Pile will receive a [![Deferred](https://img.shields.io/github/labels/EleutherAI/The-Pile/Deferred%20to%20v2)](https://github.com/AI-Nordics/the-nordic-pile/labels/Deferred%20to%20v2) or [![Declined](https://img.shields.io/github/labels/EleutherAI/The-Pile/Declined)](https://github.com/AI-Nordics/the-nordic-pile/labels/Declined) 
label. We will now focus on datasets in the following languages of the nordics: Swedish, Danish, Norwegian, Icelandic, Faroese and Finnish.

To claim responsibility for implementing an unclaimed dataset, 
leave a comment on one of our unassigned issues. Once a dataset 
has been assigned to you, make the necessary changes to `datasets.py` and `pile.py` 
in a fork and submit a pull request. If you require, you can also 
submit a script for processing the data as shown [here](https://github.com/EleutherAI/pile_enron_emails).

To raise an issue that is not proposing a new dataset, 
open an issue with the tag [![Feature Request](https://img.shields.io/github/labels/EleutherAI/The-Pile/Feature%20Request)](https://github.com/EleutherAI/The-Pile/labels/Feature%20Request) or [![Bug](https://img.shields.io/github/labels/EleutherAI/The-Pile/Bug)](https://github.com/ekgren/the-nordic-pile/labels/Bug) as appropriate.

Data ready for final implementation should meet the following criteria:

- The data must be in [lm_dataformat](https://github.com/leogao2/lm_dataformat/) format.
- The data must be shuffled.

## Attribution
This initiative is heavily inspired by Eleuther AIs The Pile project.  
[https://www.eleuther.ai/](https://www.eleuther.ai/)  
[https://pile.eleuther.ai/](https://pile.eleuther.ai/)  
