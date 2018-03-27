FROM alpine:3.7

MAINTAINER Cameron Blandford <cam@blandford.io>

# install python3, pip3
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# copy over all files
COPY . .

# install requirements
RUN pip3 install -r requirements.txt

# place the jobs in the system's crontabs folder
COPY jobs.txt /var/spool/cron/crontabs/root

# add log
RUN touch /log.txt

# give execution rights to bash script and crontab file
RUN chmod +x /var/spool/cron/crontabs/root
RUN chmod +x /doit

# Run the command on container startup
# -L: specify output file for logs
# -l: specify verbosity of logs
# -f: run in foreground
CMD ["crond", "-L", "/log.txt", "-l", "2", "-f"]
