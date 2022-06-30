.PHONY: help
help: Makefile
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: run ngc pytorch
ngc-pytorch: ## run ngc pytorch image
	docker run --rm -it --gpus all -v $(shell pwd):/workspace -p 8889:8889 --name ngc-pytorch nvcr.io/nvidia/pytorch:22.06-py3 

.PHONY: run pytorch/pytorch 11.1
pytorch: ## run pytorch/pytorch 11.1 image
	docker run --rm -it --gpus all -v $(shell pwd):/workspace -p 8888:8888 --name torch pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel

.PHONY: run denseflow
denseflow: 
	docker run --rm --gpus all --name denseflow -v $(pwd):/workspace lantgabor/denseflow:latest
