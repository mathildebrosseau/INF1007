
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = int(secondes/31557600)

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = int((secondes-(annees*31536000))/604800)

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = int((secondes-(annees*31536000)-(semaines*604800))/86400)

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = int((secondes-(annees*31536000)-(semaines*604800)-(jours*86400))/3600)

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = int((secondes-(annees*31536000)-(semaines*604800)-(jours*86400)-(heures*3600))/60)

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = int((secondes-(annees*31536000)-(semaines*604800)-(jours*86400)-(heures*3600)-(minutes*60)))

    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(f"{annees} années, {semaines} semaines, {jours} jours, {heures} heures, {minutes} minutes et {secondes} secondes.")
    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    decomposer(secondes)
