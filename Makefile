.SILENT:

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

test:clean
	PYTHONPATH=. python -m doctest custom_list.py
	PYTHONPATH=. python -m doctest car_shop.py
	PYTHONPATH=. python -m doctest model.py
