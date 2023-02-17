# INSTALLING

The following instructions target Ubuntu 20.04 LTS and Ubuntu 22.04 LTS; but, with some minor changes, should also apply to Linux distribution that uses `systemd` to manage services. Python 3.8 or newer is required and the system must already have a working installation available.

This document provides instructions on how to serve the application through [Gunicorn](https://gunicorn.org) and use [NGINX](https://nginx.org/) as a front-end HTTP server. Other options are available for serving up applications built using Flask, but those options will not be covered here.

## Installing the Application

Clone a copy of this repository to a location of your choosing by running:

```bash
git clone https://github.com/questionlp/stats.wwdt.me_v5.git
```

Within the new local copy of the repository, create a new virtual environment and install the required packages by running the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -U pip setuptools wheel
pip install -r requirements.txt
```

Next, make a copy of the `config.json.dist` file and name it `config.json`. Edit the `config.json` file and fill in the required database connection information and any other settings that are specific to your environment.

To validate the installation, start up `gunicorn` using the following command while in the application root directory and with the virtual environment activated:

```bash
gunicorn stats:app --reload
```

Once started, open a browser and browse to <http://127.0.0.1:8000/>. This should bring up the Stats Page web application.

## MySQL sql_mode Flags

Earlier versions of the Stats Page application included SQL queries that were written to target MySQL 5.5 and MariaDB 10.x. Some of the queries may throw errors due to violation of the `sql_mode` flag `ONLY_FULL_GROUP_BY` on newer versions of MySQL. These SQL queries should already be updated to resolve such errors.

In case these errors persist when running older versions of the Stats Page application, the `ONLY_FULL_GROUP_BY` flag needs to be removed from the global `sql_mode` variable. To verify which flags are currently set, you will first need to query the current value of `sql_mode` by running:

```sql
select @@sql_mode;
```

In order for the flag to be set on MySQL service startup, you will need to update the `mysqld.cnf` file on the server with the following configuration line and then restart the service.

```text
sql-mode = <flags>
```

## Configuring Gunicorn

Gunicorn can take configuration options either as command line arguments or it can load configuration options from a `gunicorn.conf.py` file located in the same directory that Gunicorn is launched from.

A template configuration file is included in the repository called `gunicorn.conf.py.dist`. A copy of that file should be made and named `gunicorn.conf.py` and the configuration options reviewed. The following options may need to be changed depending on the environment in which the application is being deployed:

* `bind`: The template defaults to using a UNIX socket file at
`/tmp/gunicorn-wwdtmstats.sock` as the listener. If TCP socket is preferred, change the value to `IP:PORT` (replacing `IP` and `PORT` with the appropriate IP address of the interface and TCP port to listen to)
* `workers`: The number of processes that are created to handle requests.
* `accesslog`: The file that will be used to write access log entries to. Change the value from a string to `None` to disable access logging if that'll be handled by NGINX or a front-end HTTP server.
* `errorlog`: The file that will be used to write error log entries to. Change the value from a string to `None` to disable error logging (not recommended). The directory needs to be created before running the application.

For more information on the above configuration options and other configuration options available, check out the [Gunicorn documentation site](https://docs.gunicorn.org/en/stable/settings.html).

## Setting up a Gunicorn systemd Service

A template `systemd` service file is included in the repository named `gunicorn-wwdtmstats.service.dist`. That service file provides the commands and arguments used to start a Gunicorn instance to serve up the application. A copy of that template file can be modified and installed under `/etc/systemd/system`.

For this document, the service file will be installed as `gunicorn-wwdtmstats.service` and the service name will be `gunicorn-wwdtmstats`. The service file name, thus the service name, can be changed to meet your needs and requirements.

You will need to modify the following items in the new service file:

* `User`: The user which the service will run under
* `Group`: The group which the service will run under
* `WorkingDirectory`: Provide the full path to the application root directory. **Do not** include the `app` directory in the path
* `Environment`: Add the full path to the `venv/bin` directory
* `ExecStart`: Include the full path to the `venv/bin` directory and insert that between `ExecStart=` and `gunicorn`

Save the file and run the following commands to enable and start the new service:

```bash
sudo systemctl enable gunicorn-wwdtmstats
sudo systemctl start gunicorn-wwdtmstats
```

Verify that the service started by running the following command:

```bash
sudo systemctl status gunicorn-wwdtmstats
```

## Serving the Application Through NGINX

Once the service is up and running, NGINX can be configured to proxy requests to Gunicorn. NGINX can also be set up to cache responses and provide additional access controls that may not be feasible with Gunicorn.

Add the following NGINX configuration snippet either to your base `nginx.conf` or to a virtual site configuration file. The configuration settings provides a starting point for serving up the application.

```nginx
upstream gunicorn-wwdtmstats {
    server unix:/tmp/gunicorn-wwdtmstats.sock fail_timeout=0;
}

server {
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass http://gunicorn-wwdtmstats;
    }
}
```

NGINX can also be configured to cache rendered pages to quickly serve up pages that are commonly and frequently requested. NGINX has documentation on configuring and enable proxy caching in their [ngx_http_proxy_module](https://nginx.org/en/docs/http/ngx_http_proxy_module.html) module documentation.
