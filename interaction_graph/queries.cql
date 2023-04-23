// Create Offers
CALL apoc.load.json('https://raw.githubusercontent.com/MohamedGouaouri/job2user_rec/main/data/offers.json') YIELD value
WITH value
MERGE (offer: Offer{offer_id: value.offer_id})
SET offer.offer_id = value.offer_id
SET offer.offer_title = value.offer_title
SET offer.offer_skills = value.offer_skills


// Create Users
CALL apoc.load.json('https://raw.githubusercontent.com/MohamedGouaouri/job2user_rec/main/data/cvs.json') YIELD value
WITH value
MERGE (user: User{cv_id: value.cv_id})
SET user.cv_id = value.cv_id
SET user.cv_title = value.cv_title
SET user.cv_skills = value.cv_skills
