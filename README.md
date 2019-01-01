# HCI Project-PhotoGlue
### Program created through Pyqt5 and based on a MILP for the arrangement of rectangular elements in a rectangular space, taking into account the aspect ratio of each element.

##### Objective of this project

The project objective is the study of an optimization problem. This problem is the collocation of elements in a rectangular space: the elements must fill the area on the space as much as possible, respecting specified constraints based on the elements number, the characteristics of the rectangular area, the initial dimensions and the importance of the elements.
Some implementations were tested to find problem solutions and subsequently discarded because of inconsistent or non optimal results. At the end, an implementation which considers the aspect ratio of each element and keeps it unchanged was chosen among many others. The reason is that this implementation let the user find a good solution in few seconds. In addition, the user can decide the execution time of the algorithm, in order to find better solution, and he can also choose among more than one solution provided by the implementation.

###### For more informations about the MILP, it is recommended to read the file "MILP-Relation.pdf".

##### Objective of PhotoGlue

The PhotoGlue idea comes from the necessity of a program that would use the considered optimization algorithm. The PhotoGlue aim is to create collages of some photos which are selected by the user. In this case, the elements of the optimization problem are the photos and the rectangular space is a background image which is chosen by the user.

###### For more informations about how to use PhotoGlue, it is recommended to see the file "PhotoGlue-Instructions For Use.odp".

##### Packages installation

The following packages are needed to use the optimization algorithm which is in the file "OptimizationProblem/MilpCplex.py" (in the brackets there is the used version of each package in this project):

- PYTHON (3.6.6);
- CPLEX (Community Edition 12.8);
- NUMPY (1.15.4).

The following packages are needed to use PhotoGlue:

- PYQT (5.9.2);
- PILLOW(5.3.0);
- the needed packages for the optimization algorithm.

##### Important notes

The Operating System used for the project development is Ubuntu. If the user wants to use the application on an other Operating System (like Windows), he needs to modify the files path in the project code: the path inserting policies are different depending on the used Operating System.
