def exercice2(expression):
    #TODO: retourner la valeur adéquate

    is_correct = True
    liste = list(expression)

    if liste.count("(") != liste.count(")"):
        is_correct = False
    else:
        for i in range(len(expression)):
            if liste[0:i].count("(") < liste[0:i].count(")"):
                is_correct = False
                break
            if is_correct == True and expression[i-1] == "(" and expression[i] == ")":
                liste.insert((i + liste.count(".")), ".")
    return "".join(liste) if is_correct == True else "Incorrect"


if __name__ == '__main__':
        expression = input("veuillez entrer l'expression : ")
        print(exercice2(expression))