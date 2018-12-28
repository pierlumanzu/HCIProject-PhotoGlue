import cplex
import numpy

def setProblemData(problem, n, informationElements, weigths, W, H):

    problem.set_problem_name("miqpex")

    problem.objective.set_sense(problem.objective.sense.maximize)

    nVariables = 2 * n ** 2 + n
    countConstraint = 0

    # NAME, TYPE, LOWER AND UPPER BOUND OF VARIABLES
    namesVariables = []
    typesVariables = ""
    lbsVariables = []
    ubsVariables = []

    for i in range(nVariables):
        if i % 3 == 2 and i < 3 * n:
            namesVariables.append("s_{}".format(i // 3))
            lbsVariables.append(0)
            typesVariables = typesVariables + "C"
            ubsVariables.append(cplex.infinity)
        else:
            if i < 3 * n:
                if i % 3 == 0:
                    namesVariables.append("x_{}".format(i // 3))
                else:
                    namesVariables.append("y_{}".format(i // 3))
                typesVariables = typesVariables + "C"
                lbsVariables.append(0)
                ubsVariables.append(cplex.infinity)
            else:
                namesVariables.append("S_{}".format(i - 3 * n))
                typesVariables = typesVariables + "B"
                lbsVariables.append(0)
                ubsVariables.append(1)

    # CONSTRAINT DEFINITION
    cols = []

    for i in range(nVariables):
        cols.append([])

        cols[i].append([])
        cols[i].append([])

    # FILL AND CONTAINMENT CONSTRAINT
    rhs = []
    senses = ""

    for i in range(n):
        for j in range(n):
            if weigths[i] >= weigths[j] and i != j:
                rhs.append(0)
                senses = senses + "L"

                cols[3 * i + 2][0].append(countConstraint)
                cols[3 * i + 2][1].append(1)

                cols[3 * j + 2][0].append(countConstraint)
                cols[3 * j + 2][1].append(-(weigths[i] / weigths[j]))

                countConstraint += 1

                rhs.append(0)
                senses = senses + "L"

                cols[3 * i + 2][0].append(countConstraint)
                cols[3 * i + 2][1].append(-1)

                cols[3 * j + 2][0].append(countConstraint)
                cols[3 * j + 2][1].append(weigths[i] / weigths[j])

                countConstraint += 1

    for i in range(n):
        rhs.append(W)
        senses = senses + "L"

        cols[3 * i][0].append(countConstraint)
        cols[3 * i][1].append(1)

        cols[3 * i + 2][0].append(countConstraint)
        cols[3 * i + 2][1].append(informationElements[i][0])

        countConstraint += 1

        rhs.append(H)
        senses = senses + "L"

        cols[3 * i + 1][0].append(countConstraint)
        cols[3 * i + 1][1].append(1)

        cols[3 * i + 2][0].append(countConstraint)
        cols[3 * i + 2][1].append(informationElements[i][1])

        countConstraint += 1

    # NO OVERLAP CONSTRAINT
    for i in range(n):
        for j in range(i + 1, n):
            countElement = 0
            for k in range(5):
                if k < 4:
                    rhs.append(0)
                    senses = senses + "L"

                    if k == 0:
                        for z in range(0, i):
                            countElement += n - (z + 1)
                        countElement *= 4
                        for z in range(i + 1, j):
                            countElement += 4
                        countElement += 3 * n

                        cols[3 * i][0].append(countConstraint)
                        cols[3 * i][1].append(1)

                        cols[3 * i + 2][0].append(countConstraint)
                        cols[3 * i + 2][1].append(informationElements[i][0])

                        cols[3 * j][0].append(countConstraint)
                        cols[3 * j][1].append(-1)

                        cols[countElement][0].append(countConstraint)
                        cols[countElement][1].append(-W)

                        countConstraint += 1
                    else:
                        if k == 1:
                            countElement += 1

                            cols[3 * j][0].append(countConstraint)
                            cols[3 * j][1].append(1)

                            cols[3 * j + 2][0].append(countConstraint)
                            cols[3 * j + 2][1].append(informationElements[j][0])

                            cols[3 * i][0].append(countConstraint)
                            cols[3 * i][1].append(-1)

                            cols[countElement][0].append(countConstraint)
                            cols[countElement][1].append(-W)

                            countConstraint += 1
                        else:
                            if k == 2:
                                countElement += 1

                                cols[3 * i + 1][0].append(countConstraint)
                                cols[3 * i + 1][1].append(1)

                                cols[3 * i + 2][0].append(countConstraint)
                                cols[3 * i + 2][1].append(informationElements[i][1])

                                cols[3 * j + 1][0].append(countConstraint)
                                cols[3 * j + 1][1].append(-1)

                                cols[countElement][0].append(countConstraint)
                                cols[countElement][1].append(-H)

                                countConstraint += 1
                            else:
                                countElement += 1

                                cols[3 * j + 1][0].append(countConstraint)
                                cols[3 * j + 1][1].append(1)

                                cols[3 * j + 2][0].append(countConstraint)
                                cols[3 * j + 2][1].append(informationElements[j][1])

                                cols[3 * i + 1][0].append(countConstraint)
                                cols[3 * i + 1][1].append(-1)

                                cols[countElement][0].append(countConstraint)
                                cols[countElement][1].append(-H)

                                countConstraint += 1

                else:
                    rhs.append(3)
                    senses = senses + "L"

                    countElement -= 3
                    for z in range(0, 4):
                        cols[countElement + z][0].append(countConstraint)
                        cols[countElement + z][1].append(1)

                    countConstraint += 1

    # LINEAR TERMS IN OBJECTIVE FUNCTION
    obj = []

    for i in range(nVariables):
        if i < 3 * n and i % 3 == 2:
            obj.append(1)
        else:
            obj.append(0)

    problem.linear_constraints.add(rhs=rhs, senses=senses)
    problem.variables.add(obj=obj, lb=lbsVariables, ub=ubsVariables, types=typesVariables, columns=cols, names=namesVariables)


def milpCplex(executionTime, n, informationElements, weigths, backgroundArea=None, W=None, H=None):
    problem = cplex.Cplex()

    problem.parameters.timelimit.set(executionTime)

    if backgroundArea is not None:

        W, H = backgroundArea.size

    else:

        if W is None and H is None:
            meanWeigthedWidth = 0
            for i in range(n):
                meanWeigthedWidth += weigths[i] * informationElements[i][0]
            meanWeigthedWidth = meanWeigthedWidth / numpy.sum(weigths)

            meanWeigthedHeight = 0
            for i in range(n):
                meanWeigthedHeight += weigths[i] * informationElements[i][1]
            meanWeigthedHeight = meanWeigthedHeight / numpy.sum(weigths)

            W = int(meanWeigthedWidth)
            H = int(meanWeigthedHeight)

    setProblemData(problem, n, informationElements, weigths, W, H)
    problem.write("OptimizationProblem/milp_cplex.lp")

    problem.solve()


    solutions = problem.solution.pool

    areas = []

    for i in range(solutions.get_num()):

        if solutions.get_objective_value(i) != 0:

            area = 0
            for j in range(n):
                area += informationElements[j][0] * informationElements[j][1] * solutions.get_values(i, 3 * j + 2)
            areas.append(area)

    areasTmp = areas[:]

    bestSolutions = []
    countSolutions = 0
    while countSolutions < 5 and len(areasTmp) != 0:
        indexMaxAreas = areas.index(max(areasTmp))
        indexMaxAreasTmp = areasTmp.index(max(areasTmp))

        bestSolutions.append([])
        bestSolutions[countSolutions].append(areasTmp.pop(indexMaxAreasTmp))

        bestSolutions[countSolutions].append([])
        for j in range(n):
            for k in range(3):
                bestSolutions[countSolutions][1].append(solutions.get_values(indexMaxAreas, 3 * j + k))

        countSolutions += 1

    return bestSolutions, W, H
