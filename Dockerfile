FROM alpine:3.7

MAINTAINER Cameron Blandford <cam@blandford.io>

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

COPY . .

RUN pip3 install -r requirements.txt

COPY jobs.txt /var/spool/cron/crontabs/root

RUN touch /log.txt

RUN chmod +x /var/spool/cron/crontabs/root
RUN chmod +x /doit
#
# RUN pip install -r requirements.txt
# # Give execution rights on the cron job
# RUN chmod 644 /etc/crontab
#
# # Run the command on container startup
CMD ["crond", "-L", "/log.txt", "-l", "2", "-f"]
