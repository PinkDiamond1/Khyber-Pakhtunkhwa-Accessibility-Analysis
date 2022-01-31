# README

This folder contains the final notebooks for the Poverty and Equity GP's spatial analysis support to two large investment projects in Khyber Pakhthunkhwa, Pakistan. One focused on prioritizing road investments amongst a variety of proposed options based on observed improvements in accessibility to markets, health facilities, and schools. The other looks to prioritize tehsils and communities for engagement in a participatory investment process based on observed access difficulties, exposure to natural risks, and low living standards. These notebooks describe the various steps taken to model accessibility in the present day and after proposed transport investments, and to rank tehsils/investments according to observed deprivations and measured potential improvements.

### Repository structure

Code for this assignment was organized within Jupyter notebook as these are comfortable environments for geographers, data scientists, and increasingly economists to develop and test complex (spatial) analyses. The only exceptions are functions that were used repeatedly and hence best represented as standalone python files -- essentially mini-libraries for the project.

The standalone python files are in the **src/custom** folder of libraries in the root directory.

The notebooks are organized in sub-folders by functionality under **notebooks**. Each folder contains a README stating any assumptions and need-to-know information for using the notebooks. The anticipated order of operations is:

1. Data Prep
2. Friction Surface
3. Access Modeling OR Roadbuilding Scenario Evaluation
4. Post Processing

Etc. contains useful code we developed but ended up not using.

### Environment Setup

This work was done using python 3.8.0 on Anaconda instances running in a Windows virtual machine. We have enclosed a *requirements.txt* file listing all the python libraries referenced. We cannot guarantee these will work out of the box on UNIX or other systems; budget time accordingly.

### Reuse

Significant effort was expended to clean up and generalize the friction surface, access modeling, and road building scenario evaluation notebooks. This was done with the expectation that these are the most complex, hard-to-repeat, and valuable components of the work. Note that the "Friction to Access" notebook is in both the friction surface and access modeling folders as it's used in both processes.

By contrast, the data preparation, post processing, and "etc" notebooks were uploaded as-is after only a brief review to remove PII and any confusing holdover code. We hope these provide useful models for others looking to implement similar or related work, but the onus of adaptation is firmly on users.

In all notebooks no effort was made to generalize folder paths -- for libraries, data inputs, or data exports -- or file names. These vary so much by project we preferred to leave them for users to adjust.

### Concepts

Reusing the work here will be hard even for experienced geographers without a firm understanding of the conceptual background. We recommend reading https://openknowledge.worldbank.org/handle/10986/35073 for details. These notebooks essentially implement a more complicated version of that process, adapted to the realities of Khyber Pakhtunkhwa instead of Karnali.
