FROM registry.baidubce.com/paddlepaddle/serving:0.9.0-devel
WORKDIR /workspaces/OCR/
COPY . /workspaces/OCR/
CMD bash