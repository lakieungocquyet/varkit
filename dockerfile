FROM continuumio/anaconda3:latest
WORKDIR /home/varkit
COPY environment.yml /home/varkit/environment.yml
COPY ./run/ /opt/deepvariant/bin/
RUN conda env create -f /home/varkit/environment.yml && \
    conda clean -afy && \
    conda config --set auto_activate_base false && \
    echo "conda activate varcall" >> ~/.bashrc



    