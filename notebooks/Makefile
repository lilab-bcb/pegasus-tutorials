BUILD_DIR=../docs/_static/tutorials

all:
	for file in ./*.ipynb; do \
		jupyter nbconvert $${file} --to html --output-dir $(BUILD_DIR) ; \
	done

clean:
	rm -f $(BUILD_DIR)/*.html
