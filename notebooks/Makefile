BUILD_DIR=../html

all:
	for file in ./*.ipynb; do \
		jupyter nbconvert $${file} --to html --output-dir ../html ; \
	done

clean:
	rm -f $(BUILD_DIR)/*.html
