# https://docs.python.org/3/library/pickle.html
# . DAT files contain binary text, and programs that use
# this data often automatically create these files
from __future__ import annotations

import pickle

d = {"some key": 12445}

with open("my_data.bin", "wb") as f:
    pickle.dump(d, f)

d_bytes = pickle.dumps(d)
print(d_bytes)

with open("my_data.bin", "rb") as f:
    db = pickle.load(f)

print(db)
print(pickle.loads(d_bytes))
