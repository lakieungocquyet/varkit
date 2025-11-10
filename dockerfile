FROM continuumio/anaconda3:latest
WORKDIR /home/varcall
COPY environment.yml /home/varcall/environment.yml
COPY ./run/ /opt/deepvariant/bin/
RUN conda env create -f /home/varcall/environment.yml && \
    conda clean -afy && \
    conda config --set auto_activate_base false && \
    echo "conda activate varcall" >> ~/.bashrc



    