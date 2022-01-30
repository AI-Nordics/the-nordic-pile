
# The Nordic Pile creation    

For now we will start gathering text data in this google drive map:
https://drive.google.com/drive/folders/1NCXyhQjocshHbbTponb68tU0baIVqK8X

So click this link and request access with a short word about your data you want to upload. You will receive access and then you can dump the data that you have.

Once we have a view on the currently available data, we can look into processing and public redistribution! :rocket:

This project is still in an early stage so feel free to drop a comment about anything or join the project because we can only create this with everyone's input. There is also a channel available on Discord for smoother communication: https://discord.gg/xVthZC9GW3. If you would like to have strong influence on the structure of the data and the distribution method afterwards. Feel free to write this in the Discord channel such that we can setup a meeting all together to get the best possible structure for this dataset.

```diff
+ Github and readme is still work in progress.
```

The Nordic Pile is a repository with the aim of providing tools and code to download and
replicate a large nordic language dataset. The dataset consists of many smaller datasets combined together.
With the objective to cover a broad set of language modalities.

---
## Ignore: Workflow For Future Plans, when spreading to a wider public!
To propose a new dataset to be added to the Nordic Pile, [open an issue](https://github.com/AI-Nordics/the-nordic-pile/issues/new).
Your issue should include a description of the dataset, its size, what language(s) it is in, 
a link to the data, and any other relevant information. If a project manger approves your proposal, 
they will change its label to [![Datasets](https://img.shields.io/github/labels/EleutherAI/The-Pile/Dataset)](https://github.com/AI-Nordics/the-nordic-pile/labels/Dataset) and add it to [![Project: Datasets](https://img.shields.io/badge/Project-Datasets-lightgrey)](https://github.com/AI-Nordics/the-nordic-pile/projects/1). Datasets that we elect to not include in the current version of the Pile will receive a [![Deferred](https://img.shields.io/github/labels/EleutherAI/The-Pile/Deferred%20to%20v2)](https://github.com/AI-Nordics/the-nordic-pile/labels/Deferred%20to%20v2) or [![Declined](https://img.shields.io/github/labels/EleutherAI/The-Pile/Declined)](https://github.com/AI-Nordics/the-nordic-pile/labels/Declined) 
label. We will now focus on datasets in the following languages of the nordics: Swedish, Danish, Norwegian, Icelandic, Faroese and Finnish.

To claim responsibility for implementing an unclaimed dataset, 
leave a comment on one of our unassigned issues. Once a dataset 
has been assigned to you, you can start:
- Join our Huggingface organisation: https://huggingface.co/organizations/AI-Nordics/share/VDyFslkvTFWzdlaQxsGJZaotESdLWKgaFV
- upload the dataset to Huggingface: Copying the example dataset ... (TODO, can we have a reviewing phase in HuggingFace, and leave out the next step then? Every datasets should be selectable by name and language)


To raise an issue that is not proposing a new dataset, 
open an issue with the tag [![Feature Request](https://img.shields.io/github/labels/EleutherAI/The-Pile/Feature%20Request)](https://github.com/EleutherAI/The-Pile/labels/Feature%20Request) or [![Bug](https://img.shields.io/github/labels/EleutherAI/The-Pile/Bug)](https://github.com/ekgren/the-nordic-pile/labels/Bug) as appropriate.

Data ready for final implementation should meet the following criteria:

- The data must be in jsonlines having the obligated fields id and text, while in meta you can add any information .<br />
 {**id = ..., text = ...,** meta={field1=..., field2=...}}
- The data must be shuffled. (Do we want this?)

## Attribution
This initiative is heavily inspired by Eleuther AIs The Pile project.  
[https://www.eleuther.ai/](https://www.eleuther.ai/)  
[https://pile.eleuther.ai/](https://pile.eleuther.ai/)  
