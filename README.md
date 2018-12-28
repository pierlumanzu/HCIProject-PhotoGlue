# HCI Project-PhotoGlue
### Program based on a MILP for the arrangement of rectangular elements on a rectangular space, taking into account the elements aspect ratio.

##### Objective of this Project

The project objective is the study of an optimization problem. This latter one is the collocation of elements on a rectangular space: the elements must fill the maximum area on the space, respecting specified constraints based on the elements number, the characteristics of the rectangular background, the initial dimensions and the importance of elements.
Some implementations was tested to find problem solutions and subsequently discarded because of inconsistent or non optimal results. At the end, an implementation which considers the aspect ratio of each element and keeps it unchanged was chosen among many others. The reason is that this implementation let the user to find a good solution in few seconds. In addition, the user can decide the execution time of the algorithm, in order to find better solution, and he can also choose among more than one solutions provided by the implementation.

###### For more informations about the MILP, it is recommended to read the file "MILP Relation.pdf".

##### Objective of PhotoGlue

The PhotoGlue idea comes from the necessity of a program that would use the considered optimization problem implementation. The PhotoGlue aim is to create some collages of some photos which are selected by the user. In this case, the elements of the optimization problem are the photos and the rectangular space are a background image which is chosen by the user.

###### For more informations about how to use PhotoGlue, it is recommended to see the file "PhotoGlue-Instructions For Use.odp".

##### Packages Installation

The following packages are needed to use the optimization algorithm (in the brackets there is the used version of each package in this project):

- CPLEX (Community Edition 12.8);
- NUMPY (1.15.4).

The following packages are needed to use PhotoGlue:

- PYTHON (3.6.6);
- PYQT (5.9.2);
- PILLOW(5.3.0);
- the needed packages for the optimization algorithm.
