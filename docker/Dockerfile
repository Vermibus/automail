FROM centos:latest

# Install epel repo
RUN yum install -y epel-release

# Install required software
COPY docker/files/requirements /files/requirements
RUN yum install -y $(cat /files/requirements)

# Install pypi dependencies
RUN easy_install-3.6 pip
COPY docker/files/pip_requirements /files/pip_requirements
RUN python36 -m pip install -r /files/pip_requirements

# Copy mutt config and automail code.
COPY docker/files/muttrc /var/spool/mail/.muttrc
COPY code /files/code

# ENTRYPOINT
COPY docker/files/entrypoint.py /files/entrypoint.py
ENTRYPOINT ["/usr/bin/python36"]
CMD ["/files/entrypoint.py"]
