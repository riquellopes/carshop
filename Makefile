.SILENT:

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

test:clean
	python -m doctest custom_list.py
	python -m doctest car_shop.py
	python -m doctest model.py
