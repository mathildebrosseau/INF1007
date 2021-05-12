import json


def create_vocabulary():
    # les mails contient la structure de donnée présente dans mail.json
    with open("mails.json") as json_data:
        emails = json.load(json_data)

    # TODO: Affécté à la variable 'result' le résultat final

    result_ham = dict()
    result_spam = dict()
    occurence_mot_spam = {}
    occurence_mot_ham = {}
    nb_mots_total_spam = 0
    nb_mots_total_ham = 0

    for this_email in emails:
        contenu_mail = this_email["mail"]
        body_mail = contenu_mail["Body"]
        if contenu_mail["Spam"] == "true":
            nb_mots_total_spam += len(body_mail)
            for word in body_mail:
                if word in occurence_mot_spam:
                    occurence_mot_spam[word] += 1
                else:
                    occurence_mot_spam[word] = 1
        else:
            nb_mots_total_ham += len(body_mail)
            for word in body_mail:
                if word in occurence_mot_ham:
                    occurence_mot_ham[word] += 1
                else:
                    occurence_mot_ham[word] = 1

    for word in occurence_mot_spam:
        prob_spam = occurence_mot_spam[word] / nb_mots_total_spam
        result_spam[word] = prob_spam

    for word in occurence_mot_ham:
        prob_ham = occurence_mot_ham[word] / nb_mots_total_ham
        result_ham[word] = prob_ham

    result = {"Spam": result_spam,
              "Ham": result_ham}

    with open('results.json', 'w') as fp:
        json.dump(result, fp, indent=4)


if __name__ == '__main__':
    create_vocabulary()
