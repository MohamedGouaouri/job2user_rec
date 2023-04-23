import json


def cv_exists(cvs, cv):
    found = False
    for cv_ in cvs:
        if cv_['cv_id'] == cv['cv_id']:
            found = True
            return found
    return found


with open("data/eval.json") as fp:
    data = json.load(fp)


offers = []
cvs = []
for offer in data:
    for cv in offer['ranked_cvs']:
        if not cv_exists(cvs, cv):
            cvs.append(cv)
    del offer['ranked_cvs']
    offers.append(offer)


with open('data/offers.json', 'w') as offer_fp:
    json.dump(offers, offer_fp)

with open('data/cvs.json', 'w') as cvs_fp:
    json.dump(cvs, cvs_fp)
