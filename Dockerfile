FROM registry.baidubce.com/paddlepaddle/serving:0.9.0-devel
WORKDIR /workspace
COPY . /workspace
RUN cd /workspace && pip3 install -r requirements.txt && python3 ./setup.py
CMD bash