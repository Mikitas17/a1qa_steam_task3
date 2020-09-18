# README #

pip install -r requirements.txt

#### To run all the tests: ####

pytest test_steam_store.py

#### To run only discount calculation tests: ####

pytest -s -v -m discount_calculation test_steam_store.py

#### To run all but discount calculation tests: ####

pytest -s -v -m "not discount_calculation" test_steam_store.py