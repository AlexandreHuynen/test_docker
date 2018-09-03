FROM python:3.6

COPY resolv.conf /etc/resolv.conf

RUN cat etc/resolv.comf

#########################################################################
# Install git
RUN apt-get update
RUN apt-get install -y git

# Add credentials on build
ARG SSH_PRIVATE_KEY
RUN mkdir /root/.ssh/
RUN echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa

RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan git.gem.myengie.com >> /root/.ssh/known_hosts
########################################################################

ARG GEMS_KEYS
#RUN echo "${GEMS_KEYS}" > /root/GEMS_KEYS.yaml
RUN echo "${GEMS_KEYS}" > /root/gems_api.yml

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD ["python", "feeder.py"]
