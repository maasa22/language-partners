# pipenv shell
# pipenv install firebase-admin
# https://qiita.com/yusukeito58/items/c77feaa25fbbe37e9953

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
import datetime
import random

# Use a service account
cred = credentials.Certificate('./language-partners-web-292104-7e6d560f966b.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Delete data
def deleteData():
    users_ref = db.collection(u'messages')
    docs = users_ref.limit(100).get()
    for doc in docs:
        print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
        doc.reference.delete()

deleteData()
